import pathlib
import unittest

from selenium import webdriver


class TestKlasa(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(pathlib.Path("D:\\repositories\\learning\\chromedriver\\chromedriver.exe"))

    def test_one(self):
        return

    def tearDown(self):
        self.driver.close()
