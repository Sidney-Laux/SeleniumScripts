import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)

        # Open Page
        login_page.open_url()

        # Fill username, password and press submit button
        login_page.execute_login("student", "Password123")

        logged_in_page = LoggedInSuccessfullyPage(driver)

        # Verify URL
        assert logged_in_page._expected_url == logged_in_page.current_url, "Actual URL is not the same as expected."

        # Verify header text
        assert logged_in_page._header == "Logged In Successfully", "Header is not expected"

        # Verify logout button is displayed
        assert logged_in_page._is_logout_button_displayed(), "Logout button is not displayed"
