import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from API.test_framework.data.email.real_email import super_user, password, valid_emails, email_for_api_user
from API.test_framework.steps.steps_api import ApiSteps
from UI.test_framework.pages.main_pages.main_page import MainPage
from UI.test_framework.pages.profile_pages.profile_main_page import ProfileMainPage
from config import env


def pytest_addoption(parser):
    """
        Перед запуском Geckodriver(firefox) выполнить команду: pip install -U selenium
    для запуска :
        pytest -s -v --tb=short --browser_name=firefox test_conftest.py
    по умолчанию броузер 'chrome'
        pytest -s -v --tb=line test_main_page.py
    """
    parser.addoption("--browser_name", default="chrome", help="Выберите браузер: chrome или firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser = browser_set(request)
    browser.implicitly_wait(5)
    MainPage(browser).open()
    yield browser
    try:
        ProfileMainPage(browser)
    except TimeoutException as err:
        return err
    finally:
        browser.quit()

@pytest.fixture(scope="function")
def browser_with_auth(request):
    browser = browser_set(request)
    browser.implicitly_wait(5)
    MainPage(browser).open()
    MainPage(browser).auth_user(email=email_for_api_user, password=password)
    yield browser
    try:
        ProfileMainPage(browser)
    except TimeoutException as err:
        return err
    finally:
        browser.quit()

@pytest.fixture
def browser_for_delete_user(request):
    browser = browser_set(request)
    browser.implicitly_wait(5)
    MainPage(browser).open()
    yield browser
    try:
        # Авторизация суперюезра
        ApiSteps().auth_user_get_token(email=super_user, password=password)
        # Удаление данных
        ApiSteps().delete_users_api(emails=valid_emails)
    except TimeoutException as err:
        return err
    finally:
        browser.quit()


def browser_set(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name.lower() == "chrome":
        if env == "linux":
            return __create_chrome_ci()
        return __create_chrome()
    elif browser_name.lower() == "firefox" or "ff":
        return __create_firefox()
    elif browser_name.lower() == "chromium":
        return __create_chromium()
    else:
        raise ValueError(f"{browser_name} не поддерживается. --browser_name должен быть chrome или firefox")


def __create_chrome():
    browser_chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser_chrome.maximize_window()
    return browser_chrome


def __create_firefox():
    browser_firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser_firefox.maximize_window()
    return browser_firefox


def __create_chromium():
    browser_chromium = webdriver.Chrome(executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    browser_chromium.set_window_size(1280, 860)
    return browser_chromium

def __create_chrome_ci():
    chrom_options = webdriver.ChromeOptions()
    chrom_options.add_argument("--no-sandbox")
    chrom_options.add_argument("--headless")
    chrom_options.add_argument("--disable-gpu")
    chrom_options.add_argument('--disable-dev-shm-usage')
    browser_chrome = webdriver.Chrome(chrome_options=chrom_options)
    browser_chrome.set_window_size(1920, 1080)
    return browser_chrome
