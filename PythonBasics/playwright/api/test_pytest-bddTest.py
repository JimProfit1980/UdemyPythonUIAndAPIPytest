import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects import orderDetailsPage
from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils
from utils.credentials import load_credentials

scenarios("../features/orderTransaction.feature")

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('place the item order as user {user_index:d}'))
def place_item_order(playwright,user_index,shared_data):
    # Credentials come from credentials.json (git-ignored) so they never live in the feature file
    user_credentials = load_credentials()[user_index]

    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)
    shared_data["order_id"] = order_id

@given('the user is on the landing page')
def user_on_landing_page(browserInstance,shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data['login_page'] = loginPage

@when(parsers.parse('I login to portal as user {user_index:d}'))
def user_login_page(user_index,shared_data):
    user_credentials = load_credentials()[user_index]
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.loginProcess(user_credentials['userEmail'], user_credentials['userPassword'])
    shared_data['dashboard_page'] = dashboardPage

@when("navigate to orders page")
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data['dashboard_page']
    orderHistoryPage = dashboardPage.clickOrderHistoryButton()
    shared_data["order_history_page"] = orderHistoryPage


@when("select the orderId")
def select_order_id(shared_data):
    order_id = shared_data['order_id']
    orderHistoryPage = shared_data["order_history_page"]
    orderDetailsPage = orderHistoryPage.selectOrder(order_id)
    shared_data["order_details_page"] = orderDetailsPage



@then("the order message is successfully displayed")
def order_message_successfully_displayed(shared_data):
 orderDetailsPage = shared_data["order_details_page"]
 orderDetailsPage.validateOrderDisplayed(shared_data["order_id"])