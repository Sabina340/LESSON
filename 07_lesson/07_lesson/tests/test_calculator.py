from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    page = CalculatorPage(driver)

    page.open()
    page.set_delay("45")
    page.press_button("7")
    page.press_button("+")
    page.press_button("8")
    page.press_button("=")

    result = page.get_result()

    driver.quit()

    assert result == "15"
