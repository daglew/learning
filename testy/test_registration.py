"""
1. Test Case - Automate User Registration process of e-commerce website.
Steps to Automate:
1. Open this url  http://automationpractice.com/index.php and maximalize window
2. Click on sign in link.
3. Enter your email address in 'Create an account' section.
4. Click on Create an Account button.
5. Enter your Personal Information, Address and Contact info.
6. Click on Register button.
7. Validate that user is created.

"""
import logging
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFormularz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(pathlib.Path("D:\\repositories\\learning\\chromedriver\\chromedriver.exe"))

    def find_and_click(self, locator: str):
        if locator.startswith("//"):
            element = self.driver.find_element(By.XPATH, locator)
            element.click()
        else:
            element = self.driver.find_element(By.ID, locator)
            element.click()
        return element

    def find_input_and_send_keys(self, locator: str, input_keys: str):
        element = self.find_and_click(locator=locator)
        element.clear()
        element.send_keys(input_keys)

    def select_radio_button_and_check(self, locator: str):
        element = self.find_and_click(locator=locator)
        assert element.is_selected() is True, f"Element:{element} is not selected"

    def find_dropdown_and_set_value(self, locator: str, set_type: str, value):
        self.find_and_click(locator=locator)
        element = None
        if set_type == "day":
            day_xpath = set_date_of_birth_dropdown_day(day=value)
            element = self.driver.find_element(By.XPATH, day_xpath)
        elif set_type == "month":
            months_xpath = set_date_of_brith_dropdown_months(months=value)
            element = self.driver.find_element(By.XPATH, months_xpath)
        elif set_type == "year":
            year_xpath = set_date_of_brith_dropdown_year(year=value)
            element = self.driver.find_element(By.XPATH, year_xpath)
        elif set_type == "state":
            state_xpath = set_state(state=value)
            element = self.driver.find_element(By.XPATH, state_xpath)
        elif set_type == "country":
            country_xpath = set_country(country=value)
            element = self.driver.find_element(By.XPATH, country_xpath)
        else:
            logging.warning("Wrong set_type should be: day, month, year")
        element.click()

    def wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, timeout=15)
        if locator.startswith("//"):
            wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        else:
            wait.until(EC.presence_of_element_located((By.ID, locator)))

    def test_registration(self):
        logging.warning("Open this url  http://automationpractice.com/index.php and maximalize window")
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()

        logging.warning("Click on sign in link.")
        SING_IN_BUTTON = "//a[@title='Log in to your customer account']"
        self.find_and_click(locator=SING_IN_BUTTON)
        expected_title = "Login - My Store"
        title = self.driver.title
        assert title == expected_title, f"Expected title {expected_title} is not equal to title:{title}"

        logging.warning("Enter your email address in 'Create an account' section.")
        CREATE_AN_ACCOUNT_INPUT = "//input[@id='email_create']"
        CREATE_AN_ACCOUNT_BUTTON = "//button[@id='SubmitCreate']"
        email_address = "ptrye@o2.pl"

        self.find_input_and_send_keys(locator=CREATE_AN_ACCOUNT_INPUT, input_keys=email_address)

        logging.warning("Click on Create an Account button")
        self.find_and_click(locator=CREATE_AN_ACCOUNT_BUTTON)

        ACCOUNT_CREATION_FORM = "account-creation_form"
        self.wait_for_element(locator=ACCOUNT_CREATION_FORM)

        logging.warning("Enter your Personal Information, Address and Contact info.")
        RADIO_BUTTON_MR = "id_gender1"
        RADIO_BUTTON_MRS = "id_gender2"

        self.select_radio_button_and_check(locator=RADIO_BUTTON_MR)
        self.select_radio_button_and_check(locator=RADIO_BUTTON_MRS)

        FIRST_NAME_INPUT_1 = "customer_firstname"
        LAST_NAME_INPUT_1 = "customer_lastname"
        EMAIL_ADDRESS_INPUT = "email"
        PASSWORD_INPUT = "passwd"

        first_name = "Kasia"
        last_name = "Gosia"
        password = "KasiaGosia"

        self.find_input_and_send_keys(locator=FIRST_NAME_INPUT_1, input_keys=first_name)
        self.find_input_and_send_keys(locator=LAST_NAME_INPUT_1, input_keys=last_name)
        self.find_input_and_send_keys(locator=EMAIL_ADDRESS_INPUT, input_keys=email_address)
        self.find_input_and_send_keys(locator=PASSWORD_INPUT, input_keys=password)

        DATE_OF_BRITH_DROPDOWN_DAY = "days"
        DATE_OF_BRITH_DROPDOWN_MONTHS = "months"
        DATE_OF_BRITH_DROPDOWN_YEARS = "years"

        self.find_dropdown_and_set_value(locator=DATE_OF_BRITH_DROPDOWN_DAY, set_type="day", value=1)
        self.find_dropdown_and_set_value(locator=DATE_OF_BRITH_DROPDOWN_MONTHS, set_type="month", value=5)
        self.find_dropdown_and_set_value(locator=DATE_OF_BRITH_DROPDOWN_YEARS, set_type="year", value=1999)

        SING_UP_FOR_NEWSLEATTER_CHECKBOX = "newsletter"
        self.select_radio_button_and_check(locator=SING_UP_FOR_NEWSLEATTER_CHECKBOX)

        RECEIVE_SPECIAL_OFFERS_CHECKBOX = "optin"
        self.select_radio_button_and_check(locator=RECEIVE_SPECIAL_OFFERS_CHECKBOX)

        address = "JEFFERSON"
        city = "CLAY"

        FIRST_NAME_INPUT_2 = "firstname"
        LAST_NAME_INPUT_2 = "lastname"
        ADDRESS_INPUT = "address1"
        CITY_INPUT = "city"

        self.find_input_and_send_keys(locator=FIRST_NAME_INPUT_2, input_keys=first_name)
        self.find_input_and_send_keys(locator=LAST_NAME_INPUT_2, input_keys=last_name)
        self.find_input_and_send_keys(locator=ADDRESS_INPUT, input_keys=address)
        self.find_input_and_send_keys(locator=CITY_INPUT, input_keys=city)

        STATE_DROPDOWN = "id_state"
        self.find_dropdown_and_set_value(locator=STATE_DROPDOWN, set_type="state", value="Alabama")

        zip_code = "00000"
        ZIP_CODE_INPUT = "postcode"
        self.find_input_and_send_keys(locator=ZIP_CODE_INPUT, input_keys=zip_code)

        COUNTRY_DROPDOWN = "id_country"
        self.find_dropdown_and_set_value(locator=COUNTRY_DROPDOWN, set_type="country", value="United States")

        mobile_phone = "5355325"
        MOBILE_PHONE_INPUT = "phone_mobile"
        self.find_input_and_send_keys(locator=MOBILE_PHONE_INPUT, input_keys=mobile_phone)

        assing_an = "My address 2215"
        ASSIGN_AN_ADDRESS_ALIAS_INPUT = "alias"
        self.find_input_and_send_keys(locator=ASSIGN_AN_ADDRESS_ALIAS_INPUT,input_keys=assing_an)

        logging.warning("Click on Register button.")

        REGISTER_BUTTON = "submitAccount"
        self.find_and_click(REGISTER_BUTTON)

        logging.warning("Validate that user is created.")

        MY_ACCOUNT = "center_column"
        ele_my_account = self.driver.find_element(By.ID, MY_ACCOUNT)
        assert ele_my_account.is_displayed(), f"element: {ele_my_account} is not displayed"

    def tearDown(self):
        self.driver.close()


#METHODS

def set_date_of_birth_dropdown_day(day: int):
    return f"//select[@id='days']/option[@value='{day}']"


def set_date_of_brith_dropdown_months(months: int):
    return f"//select[@id='months']/option[@value='{months}']"


def set_date_of_brith_dropdown_year(year: int):
    return f"//select[@id='years']/option[@value='{year}']"


def set_state(state: str):
    return f"//option[text()='{state.capitalize()}']"


def set_country(country):
    return f"//option[text()='{country}']"



def find_and_click(locator: str):
    if locator.startswith("//"):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
    else:
        element = self.driver.find_element(By.ID, locator)
        element.click()
    return element



def find_input_and_send_keys(locator: str, input_keys: str):

    element = find_and_click(locator=locator)
    element.clear()
    element.send_keys(input_keys)
