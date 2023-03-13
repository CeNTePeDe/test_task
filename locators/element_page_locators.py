from selenium.webdriver.common.by import By


class CheckBoxPageLocators:
    EXPEND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    HOME_TOGGLE = (By.XPATH, "//button[@class='rct-collapse rct-collapse-btn']")
    DOWNLAND_TOGGLE = (By.XPATH, "//li[@class='rct-node rct-node-parent rct-node-collapsed'][last()]//button")
    DOWNLAND_WORD_FILE = (By.XPATH, "//span[text()='Word File.doc']")
    TEXT = (By.XPATH, "//span[@class='text-success']")
