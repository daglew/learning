import os
import pathlib
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class PathsForProject:
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CHROMEDRIVER_PATH = os.path.join(ROOT_DIR, "chromedriver/chromedriver.exe")


# class WebDriverTests(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(PathsForProject.CHROMEDRIVER_PATH)
#
#     def tearDown(self):
#         self.driver.close()


class TestCheckButton(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(PathsForProject.CHROMEDRIVER_PATH)

    def test_check_elements_after_adding_elements_one_click(self):
        xpath_add_button = "//button[.='Add Element']"
        xpath_delete_buttons = "//div[@id='elements']/button"
        expected_one_click = 1

        self.driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
        self.driver.maximize_window()

        add_element = self.driver.find_element(By.XPATH, xpath_add_button)
        add_element.click()
        delete_buttons = self.driver.find_elements(By.XPATH, xpath_delete_buttons)

        assert len(delete_buttons) == expected_one_click, f"length delete_buttons: {delete_buttons} not equal to " \
                                                          f"expected_one_click result: {expected_one_click} "


    def test_check_elements_after_adding_elements_two_clicks(self):
        xpath_add_button = "//button[.='Add Element']"
        xpath_delete_buttons = "//div[@id='elements']/button"
        expected_two_clicks = 2

        self.driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
        self.driver.maximize_window()

        add_element = self.driver.find_element(By.XPATH, xpath_add_button)
        add_element.click()
        add_element.click()
        delete_buttons = self.driver.find_elements(By.XPATH, xpath_delete_buttons)

        assert len(delete_buttons) == expected_two_clicks, f"length delete_buttons: {delete_buttons} not equal to " \
                                                          f"expected_two_clicks result: {expected_two_clicks} "

    def test_check_elements_after_adding_elements_two_clicks_two_deletes(self):
        xpath_add_button = "//button[.='Add Element']"
        xpath_delete_buttons = "//div[@id='elements']/button"
        expected = 0

        self.driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
        self.driver.maximize_window()

        add_element = self.driver.find_element(By.XPATH, xpath_add_button)
        for action in range(2):
            add_element.click()
        delete_buttons = self.driver.find_elements(By.XPATH, xpath_delete_buttons)

        for element in delete_buttons:
            element.click()

        delete_buttons_after_delete_elements = self.driver.find_elements(By.XPATH, xpath_delete_buttons)

        assert len(delete_buttons_after_delete_elements) == expected, f"length delete_buttons: {delete_buttons} not " \
                                                                      f"equal to expected_two_clicks result: {expected}"

    def tearDown(self):
        self.driver.close()