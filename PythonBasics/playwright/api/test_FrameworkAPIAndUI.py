import pytest
from playwright.sync_api import Playwright

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils
from utils.credentials import load_credentials

user_CredentialsList = load_credentials()

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials',user_CredentialsList)
@pytest.mark.usingparameters
def test_endTwoEndWebApis(playwright:Playwright, browserInstance, user_credentials):

    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright,user_credentials)
    print("Order ID: ", order_id)

    loginPage = LoginPage(browserInstance)
    #loginPage.navigate()

    dashboardPage = loginPage.loginProcess(user_credentials["userEmail"],user_credentials["userPassword"])
    orderHistoryPage = dashboardPage.clickOrderHistoryButton()

    orderDetailsPage = orderHistoryPage.selectOrder(order_id)
    orderDetailsPage.validateOrderDisplayed(order_id)

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













