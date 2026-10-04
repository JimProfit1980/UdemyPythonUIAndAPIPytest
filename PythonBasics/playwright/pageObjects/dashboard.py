from playwright.sync_api import expect

from .ordersHistoryPage import OrdersHistoryPage


class DashboardPage:

    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")

    def clickOrderHistoryButton(self):
        self.page.get_by_role("button", name="   ORDERS").click()

        ordersHistoryPage = OrdersHistoryPage(self.page)
        expect(ordersHistoryPage.page.get_by_role("heading", name="Your Orders")).to_be_visible()
        return ordersHistoryPage





