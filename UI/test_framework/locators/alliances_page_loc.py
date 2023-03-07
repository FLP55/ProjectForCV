from selenium.webdriver.common.by import By



class LocatorsAlliancesPage:
    create_alliance_locator = (By.XPATH, "//button[text()='Создать альянс']")
    header_create_alliance_locator = (By.XPATH, "//h2[text()='Создание альянса']")
    click_name_locator = (By.XPATH, "//label[contains(text(), 'Название альянса')]")
    input_name_locator = (By.XPATH, "//*[@id='name']")
    industry_dropdown_locator = (By.XPATH, "//*[@id='industry']")
    select_industry_locator = (By.XPATH, "//*[@id='options']/li[5]")
    input_description_locator = (By.XPATH, "//*[@id='description']")
    click_info_button_locator = (By.XPATH, "//button[@class='InfoButton_button__4uRAe']")
    check_info_button_locator = (By.XPATH, "//p[contains(text(), 'Ваш альянс')]")
    click_button_save = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    click_checkbox_open_close = (By.XPATH, "//span[contains(@class, 'MuiButtonBase-root')]")
    click_created_tab_alliance = (By.XPATH, "//span[text()='Созданные']")
    search_alliance_locator = (By.XPATH, f'//div[text()="1H4Txkfz Автотест"]')
