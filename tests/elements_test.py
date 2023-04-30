import time

from pages.elements_page import TextBoxPage


class TestElements():
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            out_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_form()
            assert full_name == out_name, "Names don't match"
            assert email == out_email, "Emails don't match"
            assert current_address == out_current_address, "Current addresses don't match"
            assert permanent_address == out_permanent_address, "Permanent addresses don't match"
