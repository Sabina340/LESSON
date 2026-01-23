from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        """
        Базовый класс страницы

        :param driver: WebDriver браузера
        """
        self.driver = driver

    def find_element(self, locator: tuple[By, str]) -> WebElement:
        """
        Находит элемент на странице

        :param locator: Кортеж (By, locator)
        :return: Найденный WebElement
        """
        return self.driver.find_element(*locator)

    def get_title(self) -> str:
        """
        Возвращает заголовок страницы

        :return: Заголовок страницы
        """
        return self.driver.title
