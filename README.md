# SauceDemo Automation Suite

Automated regression tests for the SauceDemo online purchase journey.
Built with Python, Playwright, and pytest.

## Stack
- Python 3.11+
- Playwright 1.44.0
- pytest 8.2.0

## Project Structure
saucedemo_automation/
├── tests/
│   ├── test_purchase_journey.py
│   └── test_login_negative.py
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── conftest.py
├── requirements.txt
└── README.md

## Setup & Run

### Install dependencies
pip install -r requirements.txt
playwright install chromium

### Run all tests
pytest tests/ -v

### Run with HTML report
pytest tests/ -v --html=report.html --self-contained-html

### Run in headed mode (visible browser)
pytest tests/ -v --headed

## Test Coverage
| Test                        | Type       | Status       |
|-----------------------------|------------|--------------|
| Full purchase journey        | Happy Path | Automated    |
| Locked out user login        | Negative   | Automated    |
| Wrong password login         | Negative   | Automated    |

## Credentials Used
- standard_user / secret_sauce — Happy path
- locked_out_user / secret_sauce — Negative case
