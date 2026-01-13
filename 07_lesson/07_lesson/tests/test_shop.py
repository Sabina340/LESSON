from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_total_price():
    service = Service()
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_product_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()
    cart_page.checkout()

    checkout_page.fill_form("Sabi", "Kirillova", "12345")
    total = checkout_page.get_total()

    driver.quit()

    assert total == "Total: $58.29"
