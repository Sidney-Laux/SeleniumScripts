import time
import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectusername", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_username(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)

        # Open Page
        login_page.open_url()

        # Enter username, password and tap submit button
        login_page.execute_login(username, password)

        # Verify error message text is Your username is invalid!
        assert login_page.get_error_message() == expected_error_message, "Error message was not expected"

    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type student into username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type incorrect password into password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectpassword")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your password is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"
