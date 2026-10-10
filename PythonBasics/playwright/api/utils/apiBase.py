from playwright.sync_api import Playwright, expect
from pytest_base_url.plugin import base_url

from utils.credentials import primary_user


class APIUtils:
    baseUrl = "https://rahulshettyacademy.com"
    ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "6960ea76c941646b7a8b3dd5"}]}
    loginPayLoad = {"userEmail": primary_user()["userEmail"], "userPassword": primary_user()["userPassword"]}
    authToken = ""

    def getToken(self,playwright:Playwright):
        #loginPayLoad = {"userEmail": user_credentials["userEmail"], "userPassword": user_credentials["userPassword"]}

        newContext = playwright.request.new_context(base_url=self.baseUrl)
        loginRequest = newContext.post("/api/ecom/auth/login",
                                       data=self.loginPayLoad)
        loginResponse = loginRequest.json()

        #expect(loginRequest.ok).to.be.true()
        #assert loginRequest.ok

        print("Response: ",loginResponse)

        self.authToken = loginResponse["token"]
        return self.authToken




    def createOrder(self,playwright:Playwright,user_credentials=None):

        self.authToken = self.getToken(playwright)

        api_request_context = playwright.request.new_context(base_url=self.baseUrl)
        createOrderResponse = api_request_context.post("/api/ecom/order/create-order",
                                 data=self.ordersPayLoad,
                                 headers={"Authorization":self.authToken,
                                          "Content-Type":"application/json"})

        #expect(createOrderResponse.status).to_equal(201)
        print(createOrderResponse.json())
        response_body = createOrderResponse.json()
        return response_body["orders"][0]
