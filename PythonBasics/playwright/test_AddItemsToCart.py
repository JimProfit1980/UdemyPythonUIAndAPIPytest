import time

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.addtocart
def test_coreAddItemsLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("input[id='username']").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    #use the value
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox",name="terms").check()
    page.get_by_role("button",name="Sign In").click()

    page.locator("app-card button").first.click()
    page.locator("app-card button").nth(1).click()

    expect(page.locator("a.nav-link.btn.btn-primary")).to_contain_text("Checkout ( 2 )")

    page.locator("a.nav-link.btn.btn-primary").click()

    expect(page.locator("h4.media-heading a[href]")).to_have_count(2)

@pytest.mark.childwindow
def test_childWindowOpens(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPageInfo:
        page.locator("a[class='blinkingText']").first.click()
    newPage = newPageInfo.value
    expect(newPage.get_by_text("mentor@rahulshettyacademy.com").last).to_be_visible()
    text_displayed = None
    word = ""
    # wait for it first
    expect(newPage.locator(".red").first).to_be_visible()

    text_displayed = newPage.locator(".red").first.text_content()
    word = (text_displayed or "").split("at")
    email = word[1].strip().split(" ")[0]
    print(email)

    assert email == "mentor@rahulshettyacademy.com"



   #time.sleep(15)









