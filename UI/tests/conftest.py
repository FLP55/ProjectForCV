import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType


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
    yield browser
    browser.quit()


def browser_set(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name.lower() == "chrome":
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
