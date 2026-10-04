from playwright.sync_api import expect

from .orderDetailsPage import OrderDetailsPage


class OrdersHistoryPage:

    def __init__(self,page):
        self.page = page

    def validateOrdersHistoryPage(self):
        expect(self.page.get_by_role("heading", name="Your Orders")).to_be_visible()

    def selectOrder(self,orderId):

        row = self.page.locator("tbody tr").filter(has_text=orderId)
        assert row.count() == 1

        row.get_by_role("button", name="View").click()
        self.page.wait_for_timeout(3_000)

        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage



