from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from lesson_10.pages.base_page import BasePage


class MainPage(BasePage):
    URL: str = "https://example.com"

    def __init__(self, driver: WebDriver) -> None:
        """
        Главная страница сайта

        :param driver: WebDriver браузера
        """
        super().__init__(driver)

    def open(self) -> None:
        """
        Открывает главную страницу

        :return: None
        """
        self.driver.get(self.URL)

    def get_header(self) -> WebElement:
        """
        Возвращает элемент заголовка h1

        :return: WebElement заголовка
        """
        return self.find_element((By.TAG_NAME, "h1"))

    def get_header_text(self) -> str:
        """
        Возвращает текст заголовка

        :return: Текст заголовка
        """
        return self.get_header().text
