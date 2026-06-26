import pytest
from pages.login_page import LoginPage
import os

BASE_URL = "https://www.saucedemo.com"


class TestLoginNegative:
    """
    Negative cases: Validates system correctly blocks invalid login attempts.
    Covers locked account and wrong credentials scenarios.
    """

    def test_locked_out_user_sees_error(self, page):
        """
        GIVEN a locked_out_user credential
        WHEN the user attempts to log in
        THEN a meaningful error message is displayed and login is blocked
        """
        login = LoginPage(page)
        login.navigate(BASE_URL)
        login.login("locked_out_user", "secret_sauce")

        error = login.get_error_message()
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path="screenshots/locked_out_user_error.png")

        # ASSERTION: Error message clearly communicates account is locked
        assert "locked out" in error.lower(), (
            f"Expected 'locked out' in error message, got: '{error}'"
        )
        # ASSERTION: User remains on login page — not redirected to inventory
        assert "/inventory.html" not in page.url, (
            "Locked user was incorrectly redirected to inventory page"
        )

    def test_wrong_password_shows_error(self, page):
        """
        GIVEN a valid username with an incorrect password
        WHEN the user attempts to log in
        THEN an authentication error is displayed
        """
        login = LoginPage(page)
        login.navigate(BASE_URL)
        login.login("standard_user", "wrong_password")

        error = login.get_error_message()
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path="screenshots/wrong_password_error.png")

        assert "username and password do not match" in error.lower(), (
            f"Expected credential mismatch error, got: '{error}'"

        )
