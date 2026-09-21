class ProductsPage:

    def __init__(self, page):
        self.page = page

        self.add_product = page.locator('#add-to-cart-sauce-labs-backpack')

        self.cart = page.locator('.shopping_cart_link')

    def add_backpack_to_cart(self):
        self.add_product.click()

    def open_cart(self):
        self.cart.click()        
        