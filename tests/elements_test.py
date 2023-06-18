import time

from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements():
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            out_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_form()
            assert full_name == out_name, "Names doesn't match"
            assert email == out_email, "Emails doesn't match"
            assert current_address == out_current_address, "Current addresses doesn't match"
            assert permanent_address == out_permanent_address, "Permanent addresses doesn't match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            check_box_page.get_checked_checkboxes()




