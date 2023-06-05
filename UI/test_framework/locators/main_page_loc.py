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

    #Oкно авторизации
    email_auth_field_locator = (By.XPATH, '//*[@id="email"]')
    password_auth_field_locator = (By.XPATH, '//*[@id="loginPassword"]')
    button_continue_auth = (By.XPATH, '//*[@id="root"]/section/div[1]/form/button')
    element_enter = (By.XPATH, '//*[@id="root"]/section/div[1]/form/h2')
    error_about_mismatch_email_auth = (By.XPATH, '//*[@id="root"]/section/div[1]/form/div[1]/div[1]/div[2]')
    error_about_mismatch_password_auth = (By.XPATH, '//*[@id="root"]/section/div[1]/form/div[1]/div[2]/div[2]/span')
    button_change_password = (By.XPATH, '//*[@id="root"]/section/div[1]/form/div[1]/div[2]/div[2]/a')
    field_email_for_change_password = (By.XPATH, '//*[@id="email"]')
    button_confirm_change_password = (By.XPATH, '//*[@id="root"]/section/div[1]/form/button')
    confirm_change_password = (By.XPATH, '//*[@id="root"]/section/div[1]/div[2]/div[1]')



