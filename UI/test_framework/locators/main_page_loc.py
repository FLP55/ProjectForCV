from selenium.webdriver.common.by import By


class LocatorsMainPage:
    button_registration_locator = (By.XPATH, '//a[text()="Создать аккаунт"]')
    email_field_locator = (By.XPATH, '//label[text()="Электронная почта"]')
    email_text_field_locator = (By.XPATH, '//input[@id="email"]')
    field_password_locator = (By.XPATH, '//label[text()="Пароль"]')
    password_text_field_locator_login = (By.XPATH, '//input[@id="loginPassword"]')
    password_text_field_locator_register = (By.XPATH, '//input[@id="password"]')
    button_hidden_password_locator = (By.XPATH, '//div[contains(@class, "TextInput_icon")]')
    repeat_password_field_locator = (By.XPATH, '//input[@id="passwordRepeat"]')
    button_hidden_repeat_password_locator = (By.XPATH, '//*[@id="root"]/div/form/div[4]/div[1]/div')
    checkbox_personal_data = (By.XPATH, '//span[@class="LabeledCheckbox_content__c1PGx"]')
    button_continue = (By.XPATH, '//button[text()="Продолжить"]')
    text_finish_page = (By.XPATH, '//span[text()="uiemailreg@aston.ru"]')
    button_login = (By.XPATH, '//button[text()="Войти"]')


