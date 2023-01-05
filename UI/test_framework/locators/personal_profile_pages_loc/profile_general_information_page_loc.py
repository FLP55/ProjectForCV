from selenium.webdriver.common.by import By


class LocatorsProfileGeneralInformationPage:
    profile_security_page_locator = (By.XPATH, "//*[@class='item-h0ZnP'][text()='Безопасность']")

    tab_general_information_locator = (By.XPATH, "//*[text()='Общая информация']")
    tab_security_locator = (By.XPATH, "//*[text()='Безопасность']")
    tab_notifications_locator = (By.XPATH, "//*[text()='Уведомления']")
    tab_settings_locator = (By.XPATH, "//*[text()='Настройки']")

    field_first_name_locator = (By.XPATH, "//span[text()='Имя']")
    field_last_name_locator = (By.XPATH, "//span[text()='Фамилия']")
    field_id_locator = (By.XPATH, "//span[text()='ID']")
    field_telephone_locator = (By.XPATH, "//span[text()='Телефон']")
    field_email_locator = (By.XPATH, "//span[text()='Электронная почта']")

    radio_button_resident_locator = (By.XPATH, "//label[text()='Резидент РФ']")
    radio_button_no_resident_locator = (By.XPATH, "//label[text()='Нерезидент РФ']")

