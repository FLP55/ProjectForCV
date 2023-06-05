from selenium.webdriver.common.by import By


class LocatorsProfileMainPage:
    element_profile = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/h2')
    button_user_menu = (By.XPATH, '//*[@id="root"]/main/header/label/div[2]/button')
    button_quit = (By.XPATH, '//*[@id="root"]/main/header/label/div[2]/ul/li[5]')
    confirm_quit = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[1]')
