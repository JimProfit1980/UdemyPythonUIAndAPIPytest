import time

import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect,Playwright


#Firefox use that and headed mode
def test_playwrightBasics(playwright):
    # if you use chromium you are testing in edge and in chrome, default in headless mode
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

#chromium engine in headless mode on a single context
def test_playwrightShortCut(page:Page):
    page.goto("https://www.google.com")
    page.reload()
    page.wait_for_timeout(1000)

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("input[id='username']").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    #use the value
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox",name="terms").check()
    page.get_by_role("button",name="Sign In").click()
    time.sleep(10)

def test_wrongLoginCredentials(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("input[id='username']").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning")
    # use the value
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="terms").check()
    page.get_by_role("button", name="Sign In").click()

    expect(page.get_by_text("Incorrect userna")).to_be_hidden()
    time.sleep(5)

@pytest.mark.firefox
def test_runningTestUsingFireFox(playwright):
    fireFoxBrowser = playwright.firefox.launch(headless=False)
    context = fireFoxBrowser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("input[id='username']").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    # use the value
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="terms").check()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(10)

def test_coreAddItemsLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("input[id='username']").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    #use the value
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox",name="terms").check()
    page.get_by_role("button",name="Sign In").click()

    time.sleep(10)









