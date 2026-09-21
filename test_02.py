from playwright.sync_api import sync_playwright, expect


def test_login():

    with sync_playwright() as p:

        browser = p.chromium.launch( channel="chrome", headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.locator("#user-name").fill("standard_user")

        page.locator("#password").fill("secret_sauce")

        page.get_by_role("button", name="Login").click()

        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        browser.close()