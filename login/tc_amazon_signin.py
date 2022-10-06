import time
import unittest
import helpers as HP
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class windows_11_edge(unittest.TestCase):

    # launch the browser
    def setUp(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def test_amazon_sign_in(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay
        HP.delay_1_5()

        # check the title is correct
        HP.title_check(self, driver)

        # check the url is correct
        HP.url_check(self, driver)

        # check the logo is visible
        HP.visibility_of_logo(driver)

        # hover over and click 'sign in' button
        HP.two_level_selection(driver)

        # put credentials and hit Enter
        HP.sign_in(driver)

        # assert displayed name
        HP.assert_name(self, driver)


class windows_11_chrome(unittest.TestCase):

    # launch browser
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_amazon_sign_in(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay
        HP.delay_1_5()

        # check the title is correct
        HP.title_check(self, driver)

        # check the url is correct
        HP.url_check(self, driver)

        # check the logo is visible
        HP.visibility_of_logo(driver)

        # hover over and click 'sign in' button
        HP.two_level_selection(driver)

        # put credentials and hit Enter
        HP.sign_in(driver)
        time.sleep(20)

        # assert displayed name
        HP.assert_name(self, driver)


    # browser closure
    def tearDown(self):
        self.driver.quit()
