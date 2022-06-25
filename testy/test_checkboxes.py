import pathlib
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCheckBoxes(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(pathlib.Path("D:\\repositories\\learning\\chromedriver\\chromedriver.exe"))

    def test_element_check_boxes(self):

        xpath_checkbox_1_clik = "//*[@id='checkboxes']/input[1]"
        xpath_checkbox_2_clik = "//*[@id='checkboxes']/input[2]"

        self.driver.get("http://the-internet.herokuapp.com/checkboxes")
        self.driver.maximize_window()

        checkbox_1 = self.driver.find_element(By.XPATH, xpath_checkbox_1_clik)
        checkbox_1.click()
        assert checkbox_1.is_selected() is True, "checkbox_1 is not selected"

        checkbox_2 = self.driver.find_element(By.XPATH, xpath_checkbox_2_clik)
        checkbox_2.click()
        checkbox_2.click()
        sleep(1)
        assert checkbox_2.is_selected() is True, "checkbox_2 is not selected"

    def tearDown(self):
        self.driver.close()