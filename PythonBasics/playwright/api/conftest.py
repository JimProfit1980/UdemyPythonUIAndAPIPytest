import os
import pytest
from playwright.sync_api import Playwright

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="Chrome",help="chrome or firefox")
    parser.addoption(
        "--url_name",action="store",default="https://rahulshettyacademy.com/client",help="url to open"
    )


#Global file, the filename has to be the same and can be used across the project
@pytest.fixture(scope="session")
def user_CredentialsList(request):
    return request.param

@pytest.fixture
def browserInstance(playwright:Playwright,request):
    browser_name = request.config.getoption("--browser_name")
    url_name = request.config.getoption("--url_name")
    global browser
    if browser_name == "Chrome":
        browser = playwright.chromium.launch(headless=os.getenv("CI") == "true")
    elif browser_name == "FireFox":
        browser = playwright.firefox.launch(headless=os.getenv("CI") == "true")

    newContext = browser.new_context()
    page = newContext.new_page()

    page.goto(url_name)

    #yield allows you to run the code then complete the code and come back and run code after the yield keyword (TEARDOWN)
    #request parameter allows you get access to the all the variables
    yield page
    newContext.close()
    browser.close()




    # Runs for every test
    # @pytest.fixture(scope="function")
    # def preWorkSetup():
    #     print("Setup complete")

    # Runs once per test file
    # @pytest.fixture(scope="module")
    # def preWorkSetup():
    #     print("Setup complete")

    # Runs once per class, but it must be in created in a class
    # @pytest.fixture(scope="class")
    # def preWorkSetup():
    #     print("Setup complete")

    # Runs once, but for the entire execution across multiple files can be used
    # @pytest.fixture(scope="session")
    # def preWorkSetup():
    #     print("Setup complete")