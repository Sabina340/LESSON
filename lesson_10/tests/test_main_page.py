import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from lesson_10.pages.main_page import MainPage


@allure.feature("Главная страница")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Открытие главной страницы")
@allure.description("Проверка открытия страницы и отображения заголовка")
def test_open_main_page(driver: WebDriver) -> None:
    """
    Тест открытия главной страницы
    :param driver: WebDriver браузера
    :return: None
    """
    page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        page.open()

    with allure.step("Проверить заголовок страницы"):
        assert page.get_header_text() == "Example Domain"
