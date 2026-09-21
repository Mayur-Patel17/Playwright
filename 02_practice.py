from playwright.sync_api import sync_playwright,expect
from time import sleep

with sync_playwright() as p:

    browser = p.chromium.launch(channel='chrome', headless=False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    sleep(5)

    page.locator("#user-name").fill("standard_user")
    sleep(5)

    page.locator("#password").fill("secret_sauce")
    sleep(5)

    page.locator("#login-button").click()
    sleep(5)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    print("Login Test Passed!")

    browser.close()