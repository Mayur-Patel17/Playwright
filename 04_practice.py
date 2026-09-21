from playwright.sync_api import sync_playwright,expect
from time import sleep

with sync_playwright() as p:

    browser = p.chromium.launch(channel='chrome', headless=False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")
    sleep(3)

    page.locator("#user-name").fill("standard_user")
    sleep(3)

    page.locator("#password").fill("secret_sauce")
    sleep(3)

    page.locator("#login-button").click()
    sleep(3)


    page.locator(".product_sort_container").select_option('lohi')
    sleep(2)
    
    # page.locator("#add-to-cart-sauce-labs-backpack").click()
    # sleep(2)


    # page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
    # sleep(2)


    # page.locator("#shopping_cart_container").click()
    # sleep(2)

    # page.locator("#checkout").click()
    # sleep(2)


    # page.locator("#first-name").fill("Mayur")
    # sleep(1)
    # page.locator("#last-name").fill("Patel")
    # sleep(1)
    # page.locator("#postal-code").fill("56001")
    # sleep(1)


    # page.locator("#continue").click()
    # sleep(1)

    # page.screenshot(path="checkout.png")
    # sleep(2)


    # expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # print("Login Test Passed!")

    browser.close()