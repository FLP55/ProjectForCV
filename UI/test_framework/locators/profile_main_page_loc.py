from selenium.webdriver.common.by import By


class LocatorsProfileMainPage:
    logo_JointML = (By.XPATH, "//h2[text()='Заполнение профиля']")
    name_field_locator = (By.XPATH, "//input[@id='firstName']")
    last_name_field_locator = (By.XPATH, "//input[@id='lastName']")
    middle_name_field_locator = (By.XPATH, "//input[@id='middleName']")
    phone_field_locator = (By.XPATH, "//input[@id='phone']")
    company_field_locator = (By.XPATH, "//input[@id='company']")
    position_field_locator = (By.XPATH, "//input[@id='position']")
    button_continue_locator = (By.XPATH, "//button[text()='Продолжить']")
