import pytest

from pageObjects.login import LoginPage
from utils.credentials import primary_user

userNameValue = primary_user()["userEmail"]
passwordValue = primary_user()["userPassword"]


@pytest.mark.shop
def test_iphoneDisplayedOnDashboard(browserInstance):
    loginPage = LoginPage(browserInstance)

    dashboardPage = loginPage.loginProcess(userNameValue,passwordValue)
    dashboardPage.validateProductDisplayed("iphone 13 pro")
