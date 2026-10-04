import page

from .dashboard import DashboardPage


class LoginPage:


    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def loginProcess(self,user_name,user_password):
        self.page.locator("#userEmail").fill(user_name)
        self.page.locator("#userPassword").fill(user_password)
        self.page.locator("#login").click()

        dashboardPage = DashboardPage(self.page)
        dashboardPage.navigate()
        return dashboardPage



