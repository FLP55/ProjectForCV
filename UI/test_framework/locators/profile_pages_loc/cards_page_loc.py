from selenium.webdriver.common.by import By


class LocatorsProfileCardsPage:
    button_expand_locator = (By.XPATH, "//button[@class='expand-M1khJ']")

    card_gor_classic_image_locator = (By.XPATH, "//*[text()='GoR Classic']")

    card_one_locator = (By.XPATH, "//li[@class='container-XBhb4'][1]")
    card_two_locator = (By.XPATH, "//li[@class='container-XBhb4'][2]")
    card_four_locator = (By.XPATH, "//li[@class='container-XBhb4'][4]")
    card_five_locator = (By.XPATH, "//li[@class='container-XBhb4'][5]")

    tab_information_locator = (By.XPATH, "//*[text()='Информация']")
    tab_history_locator = (By.XPATH, "//*[text()='История']")
    tab_control_locator = (By.XPATH, "//*[text()='Управление']")
