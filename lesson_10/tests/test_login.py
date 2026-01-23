import allure


from lesson_10.pages.login_page import LoginPage


@allure.title("Успешная авторизация")
@allure.description("Проверка входа пользователя с корректными данными")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_success_login(driver):
    login_page = LoginPage(driver)

    with allure.step("Открываем страницу логина"):
        login_page.open("https://example.com/login")

    with allure.step("Вводим логин и пароль"):
        login_page.login("admin", "admin123")

    with allure.step("Проверяем, что открылась главная страница"):
        assert "dashboard" in driver.current_url
