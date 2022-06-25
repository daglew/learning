import pathlib
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTwoClass(unittest.TestCase):

    def setUp(self) -> None:
        self.przegladarka = webdriver.Chrome(pathlib.Path("D:\\repositories\\learning\\chromedriver\\chromedriver.exe"))

    def test_o2_poczta_login(self):
        strona = self.przegladarka.get("https://poczta.o2.pl/zaloguj")
        self.przegladarka.maximize_window()
        tytul = self.przegladarka.title
        spodziewany_tytul = "Poczta o2 - najszybciej rozwijająca się poczta"
        assert tytul == spodziewany_tytul, \
            f"Current result is: {tytul}, different than expected one: {spodziewany_tytul}"

        login_input = "login"
        password_input = "password"
        submit_button = "//button[@type='submit']"
        regulamin = "//div/button[2]"

        username = "dxyz@o2.pl"
        password_to_send = "zaba"

        akceptuj_regulamin = self.przegladarka.find_element(By.XPATH, regulamin)
        akceptuj_regulamin.click()

        przegladarka_nazwa_uzytkownika = self.przegladarka.find_element(By.ID, login_input)
        przegladarka_nazwa_uzytkownika.clear()
        przegladarka_nazwa_uzytkownika.send_keys(username)

        przegladarka_haslo = self.przegladarka.find_element(By.ID, password_input)
        przegladarka_haslo.clear()
        przegladarka_haslo.send_keys(password_to_send)

        przycisk_zaloguj = self.przegladarka.find_element(By.XPATH, submit_button)
        przycisk_zaloguj.click()

        sleep(2)
        username_po_zalogowaniu = "//div[.='xyz.zaba']"
        nazwa_po_zalogowaniu = self.przegladarka.find_element(By.XPATH, username_po_zalogowaniu)
        nazwa_po_zalogowaniu_text = nazwa_po_zalogowaniu.text

        spodziewana_nazwa = "xyz.zaba"
        assert nazwa_po_zalogowaniu_text == spodziewana_nazwa, \
            f"nazwa po zalogowaniu:{nazwa_po_zalogowaniu_text} nie rowna sie: {spodziewana_nazwa}"




    def tearDown(self) -> None:
        self.przegladarka.close()

