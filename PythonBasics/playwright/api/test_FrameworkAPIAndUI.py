import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from pageObjects.ordersHistoryPage import OrdersHistoryPage
from utils.apiBase import APIUtils

emailAddressValue = "uncleshanie300@gmail.com"
passwordValue = "Password32112345"

with open("../api/data/credentials.json", "r") as f:
    test_data = json.load(f)
    print(test_data)

user_CredentialsList = test_data["user_credentials"]

@pytest.mark.parametrize('user_credentials',user_CredentialsList)
@pytest.mark.end2endwebapi
def test_end2EndWebApi(playwright:Playwright,user_credentials):
    browserContext = playwright.chromium.launch(headless=False)
    newContext = browserContext.new_context()
    page = newContext.new_page()

    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright,user_credentials)
    print("Order ID: ", order_id)

    loginPage = LoginPage(page)
    loginPage.navigate()

    dashboardPage = loginPage.loginProcess(user_credentials["userEmail"],user_credentials["userPassword"])
    orderHistoryPage = dashboardPage.clickOrderHistoryButton()

    orderDetailsPage = orderHistoryPage.selectOrder(order_id)
    orderDetailsPage.validateOrderDisplayed(order_id)
    page.close()

    # expect(page.get_by_role("heading", name="Your Orders")).to_be_visible()
    # orderHistoryOrderId = page.locator("tbody tr").filter(has_text=order_id)
    #
    # assert orderHistoryOrderId.count() == 1
    #
    # orderHistoryOrderId.get_by_role("button",name="View").click()
    # page.wait_for_timeout(3_000)
    #
    # expect(page.locator("p.tagline")).to_have_text("Thank you for Shopping With Us")
    # expect(page.locator("div.col-text")).to_have_text(order_id)













