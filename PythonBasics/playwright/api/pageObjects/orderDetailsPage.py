from playwright.sync_api import expect


class OrderDetailsPage:

    def __init__(self,page):
        self.page = page

    def validateOrderDetailsPage(self):
        expect(self.page.get_by_role("heading", name="Your Orders")).to_be_visible()

    def validateOrderDisplayed(self,orderId):
        expect(self.page.locator("p.tagline")).to_have_text("Thank you for Shopping With Us")
        expect(self.page.locator("div.col-text")).to_have_text(orderId)

