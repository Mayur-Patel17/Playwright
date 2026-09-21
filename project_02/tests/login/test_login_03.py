import pytest
from project_02.pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("standard_user", "wrong_password"),
        ('           ', "secret_sauce"),
    ]
)
def test_login(page, username, password):

    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)

    login_page.login(username, password)