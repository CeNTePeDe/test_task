import time

from locators.element_page_locators import CheckBoxPageLocators
from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_list(self):
        self.element_is_clickable(self.locators.HOME_TOGGLE).click()
        self.element_is_clickable(self.locators.DOWNLAND_TOGGLE).click()
        self.element_is_clickable(self.locators.DOWNLAND_WORD_FILE).click()
        time.sleep(2)

    def get_output_result(self):
        text = self.element_is_present(self.locators.TEXT).text
        return text
