"""
Please check if below text is visible on the page.
page = http://the-internet.herokuapp.com/abtest
title to check = A/B Test Variation 1
content of page = "Also known as split testing. This is a way in which businesses are able to simultaneously test
                   and learn different versions of a page to see which text and/or functionality works best towards
                   a desired outcome (e.g. a user action such as a click-through)."
"""
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTextOnPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(pathlib.Path("D:\\repositories\\learning\\chromedriver\\chromedriver.exe"))

    def test_check_text_on_page(self):
        self.driver.get("http://the-internet.herokuapp.com/abtest")
        self.driver.maximize_window()

        expected_title = "A/B Test Control"
        expected_content = "Also known as split testing. This is a way in which businesses are able to simultaneously " \
                           "test and learn different versions of a page to see which text and/or functionality works " \
                           "best towards a desired outcome (e.g. a user action such as a click-through)."

        xpath_title = "//div[@id='content']//h3"
        xpath_content = "//div[@id='content']//p"

        element_title = self.driver.find_element(By.XPATH, xpath_title)
        element_content = self.driver.find_element(By.XPATH, xpath_content)

        text_element_title = element_title.text
        text_element_content = element_content.text

        assert text_element_title == expected_title, f"text_element_title:{text_element_title} is not equal to " \
                                                     f"expected_title:{expected_title}"
        assert text_element_content == expected_content, f"text_element_cotent: {text_element_content} is not equal to" \
                                                         f"expected_content: {expected_content}"

    def tearDown(self):
        self.driver.close()
