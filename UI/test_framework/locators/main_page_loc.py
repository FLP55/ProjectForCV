from selenium.webdriver.common.by import By


class LocatorsMainPage:
    #Окно регистрации
    button_registration_locator = (By.XPATH, '//a[text()="Создать аккаунт"]')
    email_reg_field_locator = (By.XPATH, '//*[@id="email"]')
    password_reg_field_locator = (By.XPATH, '//*[@id="password"]')
    confirm_password_reg_field_locator = (By.XPATH, '//*[@id="passwordRepeat"]')
    button_continue_reg = (By.XPATH, '//*[@id="root"]/section/div[1]/form/button')
    error_about_coincidence_password = (By.XPATH, '//*[@id="root"]/section/div[1]/form/div[2]/div[3]/div[2]')
    message_about_reg_new_user = (By.XPATH, '//*[@id="root"]/section/div[1]/div[2]/div[2]')
    error_about_mismatch_email = (By.XPATH, '//*[@id="root"]/section/div[1]/form/div[2]/div[1]/div[2]')
    error_about_mismatch_password = (By.XPATH, '//*[@id="root"]/section/div[1]/form/div[2]/div[2]/div[2]/span[1]')
    #JS скрипт, для взаимодействия с псевдоэлементом
    checkbox_reg_locator = 'document.getElementsByName("checkBox")[0].click();'



    password_text_field_locator_login = (By.XPATH, '//input[@id="loginPassword"]')
    password_text_field_locator_register = (By.XPATH, '//input[@id="password"]')
    button_hidden_password_locator = (By.XPATH, '//div[contains(@class, "TextInput_icon")]')
    button_hidden_repeat_password_locator = (By.XPATH, '//*[@id="root"]/div/form/div[4]/div[1]/div')
    checkbox_personal_data = (By.XPATH, '//span[@class="LabeledCheckbox_content__c1PGx"]')
    button_continue = (By.XPATH, '//button[text()="Продолжить"]')
    text_finish_page = (By.XPATH, '//span[text()="uiemailreg@aston.ru"]')
    button_login = (By.XPATH, '//button[text()="Войти"]')


