from selenium.webdriver.common.by import By



class LocatorsCreateModel:
    button_create_model = (By.XPATH, '//*[@id="root"]/main/section[2]/div/div/div[1]/button')
    name_field = (By.XPATH, '//*[@id="name"]')
    type_field = (By.XPATH, '//*[@id="tasksType"]')
    category_field = (By.XPATH, '//*[@id="category"]')
    type_model_field = (By.XPATH, '//*[@id="modelType"]')
    description_field = (By.XPATH, '//*[@id="description"]')
    teg_bank = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/form/div[4]/div[2]/div[2]/div[3]')
    input_file = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/form/div[5]/div/input')
    button_add = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/form/button')
    type_class = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/form/div[1]/div[2]/div[1]/ul/li[1]')
    first_category = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/form/div[2]/div[1]/div[1]/ul/li[2]')
    message_about_repeated_name = (By.XPATH, '//*[@id="root"]/main/section[2]/div/section/form/div[1]/div[1]/div[2]')