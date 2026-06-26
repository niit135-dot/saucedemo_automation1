class CheckoutPage:
    def __init__(self, page):
        self.page             = page
        self.first_name       = page.locator("[data-test='firstName']")
        self.last_name        = page.locator("[data-test='lastName']")
        self.postal_code      = page.locator("[data-test='postalCode']")
        self.continue_button  = page.locator("[data-test='continue']")
        self.finish_button    = page.locator("[data-test='finish']")
        self.complete_header  = page.locator(".complete-header")
        self.complete_text    = page.locator(".complete-text")
        self.item_total_label = page.locator(".summary_subtotal_label")

    def assert_on_checkout_page(self):
        """Assert we are on checkout step one."""
        self.page.wait_for_url("**/checkout-step-one.html", timeout=8000)
        assert "/checkout-step-one.html" in self.page.url

    def enter_customer_details(self, first, last, postcode):
        """Fill in customer info and click Continue."""
        self.assert_on_checkout_page()
        self.first_name.wait_for(state="visible", timeout=5000)
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postcode)
        self.continue_button.click()

    def assert_on_order_overview(self):
        """Assert we are on checkout step two — order overview."""
        self.page.wait_for_url("**/checkout-step-two.html", timeout=8000)
        assert "/checkout-step-two.html" in self.page.url, (
            f"Expected order overview page, got: {self.page.url}"
        )

    def get_item_total(self):
        """Return item total label text e.g. 'Item total: $29.99'."""
        self.item_total_label.wait_for(state="visible", timeout=5000)
        return self.item_total_label.inner_text()

    def complete_order(self):
        """Click the Finish button to complete the order."""
        self.finish_button.wait_for(state="visible", timeout=5000)
        self.finish_button.click()

    def assert_order_confirmed(self):
        """Assert order confirmation page is shown with Thank You message."""
        self.complete_header.wait_for(state="visible", timeout=8000)
        header_text = self.complete_header.inner_text()
        assert "Thank you" in header_text, (
            f"Order confirmation not found. Got: {header_text!r}"
        )
