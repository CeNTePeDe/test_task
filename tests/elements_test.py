from pages.element_page import CheckBoxPage


class TestElements:
    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_list()
            result = check_box_page.get_output_result()
            assert result == 'wordFile', 'File has not been changed'

