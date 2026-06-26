class LoginPage:
    def __init__(self, page):
        self.page           = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button   = page.locator("[data-test='login-button']")
        self.error_message  = page.locator("[data-test='error']")

    def navigate(self, url="https://www.saucedemo.com"):
        """Navigate to the login page."""
        self.page.goto(url)

    def login(self, username, password):
        """Fill credentials and click login."""
        self.username_input.wait_for(state="visible", timeout=5000)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """Return the error message text shown on failed login."""
        self.error_message.wait_for(state="visible", timeout=5000)
        return self.error_message.inner_text()

    def assert_error_message_contains(self, expected_text):
        """Assert the error message contains the expected text."""
        error = self.get_error_message()
        assert expected_text in error, (
            f"Expected {expected_text!r} in error message, got: {error!r}"
        )

    def assert_still_on_login_page(self):
        """Assert user was NOT redirected — login was blocked."""
        assert "/inventory" not in self.page.url, (
            f"User should not have been logged in, but got: {self.page.url}"
        )
