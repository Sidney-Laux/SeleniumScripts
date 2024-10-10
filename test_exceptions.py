import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestExceptions:

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_no_such_element_exception(self, driver):
        # Navigate to Webpage
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        row2_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row2_locator.is_displayed(), "Row 2 input should be displayed but it is not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Type text into the second input field
        row2_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        row2_locator.send_keys("Instant Noodles")

        # Push Save button using locator By.name(“Save”)
        save_button_locator = driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']")
        save_button_locator.click()

        # Verify text saved
        saved_confirmation_locator = driver.find_element(By.ID, "confirmation")
        saved_confirmation_message = saved_confirmation_locator.text
        assert saved_confirmation_message == "Row 2 was saved", "Confirmation message is not expected."

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click on Edit button
        edit_button_locator = driver.find_element(By.ID, "edit_btn")
        edit_button_locator.click()

        # Clear input field
        row1_locator = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        row1_locator.clear()

        # Type text into the input field
        row1_locator.send_keys("New text")

        # Tap Save button
        save_button_locator = driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Save']")
        save_button_locator.click()

        # Verify text changed
        wait = WebDriverWait(driver, 5)
        saved_confirmation_locator = wait.until(
            expected_conditions.visibility_of_element_located((By.ID, "confirmation")))
        saved_confirmation_message = saved_confirmation_locator.text
        time.sleep(10)
        assert saved_confirmation_message == "Row 1 was saved", "Confirmation message is not expected."

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        # instruction_locator = driver.find_element(By.ID, "instructions")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 5)
        assert wait.until(expected_conditions.invisibility_of_element_located(
            (By.ID, "instructions"))), "Instructions test element should not be displayed"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)
        row2_locator = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")),
            "Failed waiting for Row 2 input to be visible")

        # Verify second input field is displayed
        assert row2_locator.is_displayed()
