import time
import random
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE

# locators
logo_id = "nav-logo-sprites"
hover_over_id = "nav-link-accountList-nav-line-1"
sign_in_class = "nav-action-inner"
email_id = "email"
password_id = "password"
continue_id = "continue"
sign_in_id = "signInSubmit"
sign_in_xpath = "//span[text()='Sign in']"

# values
url = "https://www.amazon.com/"
title = "Amazon.com. Spend less. Smile more."
email_value = "qa.test.for.test@gmail.com"
password_value = "BG_xU%ZTjRU3b&e"
assertion_name = "Hello, Test"

# set up random delay
def delay_1_5():
    time.sleep(random.randint(1, 5))

# presence of element, utility
def presence_of_elem(driver, locator_type, locator):
    wait = WebDriverWait(driver, 3)
    elem = wait.until(EC.presence_of_element_located((locator_type, locator)))
    return elem

# visibility of element, utility
def visability_of_elem(driver, locator_type, locator):
    wait = WebDriverWait(driver, 3)
    elem = wait.until(EC.visibility_of_element_located((locator_type, locator)))
    return elem

# assert page title
def title_check(self, driver):
    self.assertEqual(title, driver.title, "The title is not correct")
    print("The title is correct")

# assert page url
def url_check(self, driver):
    self.assertEqual(url, driver.current_url, "The URL is not correct")
    print("The URL is correct")

# check logo visibility
def visibility_of_logo(driver):
    try:
        presence_of_elem(driver, By.ID, logo_id)
        visability_of_elem(driver, By.ID, logo_id)
        print('The logo is visible')
    except WDE:
        print('The logo is not visible')
        driver.get_screenshot_as_file('logo_visibility_error.png')
        driver.save_screenshot('logo_visibility_error.png')

# hover over and click the button
def two_level_selection(driver):
    a = ActionChains(driver)
    try:
        a.move_to_element(
            driver.find_element(By.ID, hover_over_id)).click(driver.find_element(By.CLASS_NAME, sign_in_class)).perform()
        print("Sign In was clicked")
    except WDE:
        print("Check two level menu")
        driver.get_screenshot_as_file('two_level_menu_error.png')
        driver.save_screenshot('two_level_menu_error.png')

# put credentials and hit Enter
def sign_in(driver):
    try:
        presence_of_elem(driver, By.NAME, email_id).send_keys(email_value + Keys.ENTER)
        print("The email was sent")
        presence_of_elem(driver, By.NAME, password_id).send_keys(password_value + Keys.ENTER)
        print("The password was sent")
    except WDE:
        print('Failed sign in')
        driver.get_screenshot_as_file('sign_in_error.png')
        driver.save_screenshot('sign_in_error.png')

# assert displayed name
def assert_name(self, driver):
    displayed_name = driver.find_element(By.ID, hover_over_id).text
    self.assertEqual(displayed_name, assertion_name, "The displayed name is not correct")
    print("Successful Sign In")

