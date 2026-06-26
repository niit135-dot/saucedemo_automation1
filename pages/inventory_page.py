class InventoryPage:
    """
    Page Object for the product inventory/listing page.
    """

    def __init__(self, page):
        self.page = page
        # Targets the first product's Add to Cart button specifically
        self.add_sauce_labs_backpack = page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_icon  = page.locator(".shopping_cart_link")

    def assert_on_inventory_page(self):
        """Confirm successful login and landing on inventory page."""
        self.page.wait_for_url("**/inventory.html", timeout=8000)
        assert "/inventory.html" in self.page.url, (
            f"Expected inventory page, got: {self.page.url}"
        )

    def add_product_to_cart(self):
        """Add Sauce Labs Backpack to cart and verify badge increments."""
        self.add_sauce_labs_backpack.wait_for(state="visible", timeout=5000)
        self.add_sauce_labs_backpack.click()

    def get_cart_count(self) -> str:
        """Return cart badge number as string."""
        self.cart_badge.wait_for(state="visible", timeout=5000)
        return self.cart_badge.inner_text()

    def go_to_cart(self):
        self.cart_icon.click()
