from selenium.webdriver.common.by import By


class LocatorsProfileMainPage:
    element_profile = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/h2')
    button_user_menu = (By.XPATH, '//*[@id="root"]/main/header/label/div[2]/button')
    button_quit = (By.XPATH, '//*[@id="root"]/main/header/label/div[2]/ul/li[5]')
    confirm_quit = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[1]')
    button_edit_profile = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/form/div[1]/button')
    button_cancel_change = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/form/div[1]/div[2]/button[1]')
    button_confirm_change = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/form/div[1]/div[2]/button[2]')
    field_name = (By.XPATH, '//*[@id="firstName"]')
    field_second_name = (By.XPATH, '//*[@id="lastName"]')
    field_last_name = (By.XPATH, '//*[@id="middleName"]')
    field_phone_number = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/form/div[2]/div[4]/div[1]')
    field_phone_number_send = (By.XPATH, '//*[@id="phone"]')
    message_confirm_change = (By.XPATH, '//*[@id="root"]/main/section[2]/ul/li/p')
    error_invalid_data_field_name = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/form/div[2]/div[1]/div[2]')
    error_invalid_data_field_second_name = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/form/div[2]/div[2]/div[2]')
    error_invalid_data_field_last_name = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/form/div[2]/div[3]/div[2]')
    error_invalid_data_field_phone_number = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/form/div[2]/div[4]/div[2]')
    button_ml_model = (By.XPATH, '//*[@id="root"]/main/section[1]/div/nav/li[1]/a')