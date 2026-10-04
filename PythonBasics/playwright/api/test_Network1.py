import time

import pytest
from playwright.sync_api import Page, Playwright, expect
from utils.apiBase import APIUtils

emailAddressValue = "uncleshanie300@gmail.com"
passwordValue = "Password32112345"
fakePayLoadResponse = {"data":[],"message":"No Orders"}

 #=> api call from browser -> api call contact server return back response back to browser -> browser use response to generate html

#All the information must be captured and will be handled in this () to test a scenario you are working in
def intercept_response(route):
    route.fulfill(json= fakePayLoadResponse
    )

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6ac0cd2c2be7a8bc2b838bb0")





@pytest.mark.mockreponse
def test_MockResponse(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)

    email = page.locator("#userEmail")
    password = page.locator("#userPassword")
    login = page.locator("#login")

    email.fill(emailAddressValue)
    password.fill(passwordValue)
    login.click()

    orderHistory = page.get_by_role("button", name="   ORDERS")
    orderHistory.click()

    order_text = page.locator(".mt-4").text_content()
    print(order_text)

@pytest.mark.mockrequest
def test_MockRequestTryingToStealAnotherPersonOrderDetails(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)

    email = page.locator("#userEmail")
    password = page.locator("#userPassword")
    login = page.locator("#login")

    email.fill(emailAddressValue)
    password.fill(passwordValue)
    login.click()

    orderHistory = page.get_by_role("button", name="   ORDERS")
    orderHistory.click()

    page.get_by_role("button",name="View").first.click()

    expectedText = page.locator(".blink_me").text_content()
    print(expectedText)

    assert expectedText == "You are not authorize to view this order"

def test_SessionStorage(playwright:Playwright):
    api_utils = APIUtils()
    authToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem("token", '{authToken}');""")
    page.goto("https://rahulshettyacademy.com/client")

    orderHistory = page.get_by_role("button", name="   ORDERS")
    orderHistory.click()

    expect(page.get_by_text("Your Orders")).to_be_visible()





