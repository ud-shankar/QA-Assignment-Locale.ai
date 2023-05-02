import pytest
from selenium.webdriver.common.by import By

from Driver.driver import driver
from Pages.dashboard_screen import dashboard
from Pages.checkout_page import checkout_page
from pytest_bdd import then, scenario
from Source.conftest import wait_and_send, wait_and_click


@pytest.mark.login()
@scenario('../Features/saucedemo.feature', 'Verify user is able to login to sauce demo dashboard')
def test_login():
    pass


@pytest.mark.dashboard()
@scenario('../Features/saucedemo.feature', 'Verify user is able to add items to the cart from sauce demo dashboard')
def test_dashboard():
    pass


@pytest.mark.dashboard()
@scenario('../Features/saucedemo.feature', 'Verify user is able to checkout and place orders')
def test_checkout():
    pass


@then("User is able to view saucedemo dashboard")
def home_page_assertion():
    assert driver.find_element(By.CSS_SELECTOR, dashboard.title_dashboard).is_displayed()


@then("User is able to add items to cart")
def add_item_to_cart():
    elements = driver.find_elements(By.CSS_SELECTOR, dashboard.btn_add_to_cart)
    for i in range(0, 3):
        elements[i].click()


@then("Verify Count of items in the cart has increased")
def verify_cart_count():
    cart_count = driver.find_element(By.CSS_SELECTOR, dashboard.icn_cart).text
    assert int(cart_count) == 3


@then("Verify user is able to checkout and add user details during checkout")
def checkout():
    wait_and_click("ID", dashboard.btn_cart)
    wait_and_click("ID", checkout_page.btn_checkout)
    wait_and_send("ID", checkout_page.txt_firstname, "uday")
    wait_and_send("ID", checkout_page.txt_lastname, "shankar")
    wait_and_send("ID", checkout_page.txt_postalcode, "656789")
    wait_and_click("ID", checkout_page.btn_continue)


@then("Verify user is able to place order successfully")
def place_order():
    wait_and_click("ID", checkout_page.btn_finish)


