from utils.apiBase import APIUtils
import pytest
from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils
emailAddressValue = "uncleshanie300@gmail.com"
passwordValue = "Password32112345"

@pytest.mark.end2endwebapi
def test_end2EndWebApi(playwright:Playwright):
    browserContext = playwright.chromium.launch(headless=False)
    newContext = browserContext.new_context()
    page = newContext.new_page()

    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright)
    print("Order ID: ", order_id)

    page.goto("https://rahulshettyacademy.com/client")
    email = page.locator("#userEmail")
    password = page.locator("#userPassword")
    login = page.locator("#login")

    email.fill(emailAddressValue)
    password.fill(passwordValue)
    login.click()

    orderHistory = page.get_by_role("button", name="   ORDERS")
    orderHistory.click()

    expect(page.get_by_role("heading", name="Your Orders")).to_be_visible()
    orderHistoryOrderId = page.locator("tbody tr").filter(has_text=order_id)

    assert orderHistoryOrderId.count() == 1

    orderHistoryOrderId.get_by_role("button",name="View").click()
    page.wait_for_timeout(3_000)

    expect(page.locator("p.tagline")).to_have_text("Thank you for Shopping With Us")
    expect(page.locator("div.col-text")).to_have_text(order_id)













