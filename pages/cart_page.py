class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("[data-test='checkout']")
        self.cart_items = page.locator(".cart_item")
        self.cart_item_names = page.locator(".inventory_item_name")

    def assert_on_cart_page(self):
        self.page.wait_for_url("**/cart.html", timeout=8000)
        assert "/cart.html" in self.page.url

    def assert_item_in_cart(self, item_name):
        """Assert that a specific item is present in the cart."""
        self.page.wait_for_url("**/cart.html", timeout=8000)
        items = self.cart_item_names.all_inner_texts()
        assert item_name in items, f"Expected {item_name!r} in cart, got: {items}"

    def get_cart_item_count(self):
        return self.cart_items.count()

    def proceed_to_checkout(self):
        self.checkout_button.wait_for(state="visible", timeout=5000)
        self.checkout_button.click()
