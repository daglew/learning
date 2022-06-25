import pathlib
import unittest

from selenium import webdriver

sterownik = webdriver.Chrome(pathlib.Path("D:\\repositories\\learning\\chromedriver\\chromedriver.exe"))

class TesTClassOne(unittest.TestCase):

    def test_open_browser(self):
        strona = sterownik.get("https://www.facebook.com/")
        sterownik.maximize_window()
        tytul = sterownik.title
        spodziewany_tytul = "Facebook – zaloguj się lub zarejestruj"
        assert tytul == spodziewany_tytul, \
            f"Current result is: {tytul}, different than expected one: {spodziewany_tytul}"
        sterownik.close()

