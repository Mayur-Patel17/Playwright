from playwright.sync_api import sync_playwright,expect
from time import sleep

with sync_playwright() as p:

    browser = p.chromium.launch(channel='chrome', headless=False)

    page = browser.new_page()

    page.goto("https://web.whatsapp.com/")
    sleep(11)

    # page.locator("#user-name").fill("standard_user")
    # sleep(5)

    # page.locator("#password").fill("secret_sauce")
    # sleep(5)

    page.locator("#_r_d_").fill("vikas")

    page.locator(".x10l6tqk xh8yej3 x1g42fcv").click()
    sleep(5)

    page.locator(".selectable-text copyable-text x15bjb6t x1n2onr6").fill("ok")

    sleep(3)

    # expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # print("Login Test Passed!")

    browser.close()