import pytest
from pages.login_page     import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page      import CartPage
from pages.checkout_page  import CheckoutPage

BASE_URL = "https://www.saucedemo.com"

# -------------------------------------------------------------------
# Test Data — Dedicated automation credentials (not shared manually)
# -------------------------------------------------------------------
VALID_USER     = "standard_user"
VALID_PASSWORD = "secret_sauce"
EXPECTED_ITEM  = "Sauce Labs Backpack"
EXPECTED_PRICE = "$29.99"


class TestPurchaseJourney:
    """
    Happy path: Full purchase journey — login through to order confirmation.
    Covers the primary regression check for the online purchase flow.
    """

    def test_complete_purchase_journey(self, page):
        """
        GIVEN a valid user visits SauceDemo
        WHEN they log in, add a product, complete checkout with valid details
        THEN the order confirmation page is displayed with correct content
        """
       
 
        
        # ── STEP 1: Navigate and Login ──────────────────────────────
        login = LoginPage(page)
        login.navigate(BASE_URL)
        login.login(VALID_USER, VALID_PASSWORD)
        page.screenshot(path="screenshots/after_login.png")

        # ── STEP 2: Assert on Inventory Page ────────────────────────
        inventory = InventoryPage(page)
        inventory.assert_on_inventory_page()

        # ── STEP 3: Add Product to Cart ─────────────────────────────
        inventory.add_product_to_cart()

        # ASSERTION: Cart badge should show 1 item
        cart_count = inventory.get_cart_count()
        assert cart_count == "1", (
            f"Expected cart badge '1', got '{cart_count}'"
        )

        # ── STEP 4: Navigate to Cart ─────────────────────────────────
        inventory.go_to_cart()

        cart = CartPage(page)
        cart.assert_on_cart_page()

        # ASSERTION: Correct product is in the cart
        cart.assert_item_in_cart(EXPECTED_ITEM)

        # ── STEP 5: Proceed to Checkout ──────────────────────────────
        cart.proceed_to_checkout()

        # ── STEP 6: Enter Customer Details ───────────────────────────
        checkout = CheckoutPage(page)
        checkout.enter_customer_details(
            first    = "Test",
            last     = "Automation",
            postcode = "SW1A 1AA"
        )

        # ── STEP 7: Assert Order Overview ────────────────────────────
        checkout.assert_on_order_overview()

        # ASSERTION: Item total contains expected price
        item_total = checkout.get_item_total()
        assert EXPECTED_PRICE in item_total, (
            f"Expected price '{EXPECTED_PRICE}' in total label, got: '{item_total}'"
        )

        # ── STEP 8: Complete Order ────────────────────────────────────
        checkout.complete_order()

        # ── STEP 9: Assert Order Confirmation ────────────────────────
        checkout.assert_order_confirmed()
        page.screenshot(path="screenshots/order_confirmed.png")
