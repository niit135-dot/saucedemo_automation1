import pytest
import os
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"

@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        yield page

        # ── SCREENSHOT ON FAILURE ─────────────────────────────────
        if request.node.rep_call.failed:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{request.node.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n📸 Screenshot saved: {screenshot_path}")

        # ── TEARDOWN ──────────────────────────────────────────────
        context.clear_cookies()
        try:
            if page.url.startswith("http"):
                page.evaluate("window.localStorage.clear()")
        except Exception:
            pass

        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Makes test result available to fixtures via request.node.rep_call"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
