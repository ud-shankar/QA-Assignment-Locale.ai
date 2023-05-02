import pytest
from Driver.driver import driver
from Pages.login import login
from pytest_bdd import given, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 30)


@pytest.fixture(scope="session", autouse=True)
def posttest():                                                     #teardown at the end of every session
    yield driver
    driver.quit()    


@given("User navigates to saucedemo website")
def locus_login():
    driver.get("https://www.saucedemo.com")


@when("User enters correct username and password")
def login_credentials():
    wait_and_send("ID", login.txt_Username, "standard_user")
    wait_and_send("ID", login.txt_Password, "secret_sauce")


@when("Clicks on login button")
def click_login_button():
    wait_and_click("ID", login.btn_Login)


def wait_and_click(locator_type, locator):
    if locator_type == "CSS":
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator))).click()
    elif locator_type == "ID":
        wait.until(EC.element_to_be_clickable((By.ID, locator))).click()


def wait_and_send(locator_type, locator, text):
    if locator_type == "CSS":
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator))).send_keys(text)
    elif locator_type == "XPATH":
        wait.until(EC.presence_of_element_located((By.XPATH, locator))).send_keys(text)
    elif locator_type == "ID":
        wait.until(EC.presence_of_element_located((By.ID, locator))).send_keys(text)    


def wait_until_element_present(locator_type, locator):
    if locator_type == "CSS":
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
    elif locator_type == "XPATH":
        wait.until(EC.presence_of_element_located((By.XPATH, locator)))
