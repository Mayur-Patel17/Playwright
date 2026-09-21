from playwright.sync_api import sync_playwright, expect
from project_01.pages.login_page import LoginPage
def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)

        page = browser.new_page()
        page.goto('https://www.saucedemo.com/')

        login_page = LoginPage(page)
        login_page.login('standard_user', "secret_sauce")

        print("sucsses!")
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


        browser.close()

                                        