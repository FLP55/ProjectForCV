from selenium.webdriver.common.by import By



class LocatorsMlModels:
    button_create_model = (By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/button')
    button_model = (By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[2]/div[2]/ul[2]/li')
    button_edit_model = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/div[1]/div[2]/button[1]')
    tab_ml_models = (By.XPATH, '//*[@id="root"]/main/section[1]/div/nav/li[1]/a')
    header = (By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/h2')


    #редактирование модели
    field_name = (By.XPATH, '//*[@id="name"]')
    type_field = (By.XPATH, '//*[@id="tasksType"]')
    field_category = (By.XPATH, '//*[@id="category"]')
    field_type_model = (By.XPATH, '//*[@id="modelType"]')
    field_description = (By.XPATH, '//*[@id="description"]')
    button_save_change = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/div/form/button')
    button_submit_switch = (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[1]')