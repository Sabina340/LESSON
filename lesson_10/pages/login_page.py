from selenium.webdriver.chrome.webdriver import WebDriver
import allure

from lesson_10.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        """
        Страница авторизации (учебная)

        :param driver: WebDriver браузера
        """
        super().__init__(driver)

    def open(self, url: str) -> None:
        """
        Открывает страницу логина

        :param url: URL страницы
        :return: None
        """
        self.driver.get(url)

    @allure.step("Выполнить авторизацию пользователя")
    def login(self, username: str, password: str) -> None:
        """
        Учебный сценарий успешной авторизации.
        Симулирует переход на главную страницу после логина.

        :param username: Логин пользователя
        :param password: Пароль пользователя
        :return: None
        """
        # Проверка входных данных (учебная)
        assert username
        assert password

        self.driver.get("https://example.com/dashboard")
