from  playwright.sync_api import sync_playwright , expect
from project_02.pages.login_page import LoginPage
from project_02.pages.product_page import ProductsPage
from project_02.pages.checkout_page import CheckoutPage

def test_complete_checkout(page):
    
    page.goto('https://www.saucedemo.com/')

    login_page = LoginPage(page)

    login_page.login("standard_user",'secret_sauce')

    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

    product = ProductsPage(page)

    product.add_backpack_to_cart()

    product.open_cart()

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    page.get_by_role('button', name='Checkout').click()

    checkout_page = CheckoutPage(page)

    checkout_page.enter_customer_details('mayur', 'patel', '283853')

    checkout_page.continue_checkout()

    checkout_page.finish_order()


    expect(checkout_page.complete_message).to_have_text('Thank you for your order!')


    


