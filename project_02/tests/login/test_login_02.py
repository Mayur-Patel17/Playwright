from playwright.sync_api import expect

from project_02.pages.login_page import LoginPage


def test_valid_login(page):

    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)

    login_page.login(
        "standard_user",
        "hello_world"
    )

    # expect(page).to_have_url(
    #     "https://www.saucedemo.com/inventory.html"
    # )

    expect(
        login_page.error_message
    ).to_be_visible()