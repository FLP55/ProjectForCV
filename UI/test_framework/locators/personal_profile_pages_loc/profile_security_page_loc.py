from selenium.webdriver.common.by import By


class LocatorsProfileSecurityPage:
    button_change_password_locator = (By.XPATH, "//span[@class='text-pStQs'][text()='Изменить пароль']")
    button_change_security_question_locator = (By.XPATH, "//*[@class='text-pStQs'][text()='Изменить пароль']")

    field_current_password_locator = (By.XPATH, "//input[@name='oldPassword']")
    field_create_new_password_locator = (By.XPATH, "//input[@name='password']")
    field_confirm_new_password_locator = (By.XPATH, "//input[@name='confirmPassword']")

    button_submit_locator = (By.XPATH, "//button[@type='submit']")
    button_submit_locator_disabled = (By.XPATH, "//button[@type='submit'][@disabled]")

    text_success_change_password_locator = (By.XPATH, "//*[@class='span-OyM7u']")

    text_validation_password_locator = (By.XPATH, "//span[@class='message-qcCa_ message-error-Rscxs']")
    text_message_missmatch_passwords_locator = (By.XPATH, "//span[@class='message-qcCa_ message-error-Rscxs']")


