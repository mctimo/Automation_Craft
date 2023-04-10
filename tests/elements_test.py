import time

from pages.elements_page import TextBoxPage


class TestElements():
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            print(email)
            out_name, out_email, out_current_address, out_permanent_address = text_box_page.check_filled_form()
            assert full_name == out_name
            assert email == out_email
            assert current_address == out_current_address
            assert permanent_address == out_permanent_address
