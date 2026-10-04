import time
from _pyrepl.commands import accept

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.hideplaceholder
def test_hidePlaceholder(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractise/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    page.locator("#hide-textbox").click()

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

@pytest.mark.showplaceholder
def test_showPlaceholder(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractise")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    page.locator("#show-textbox").click()

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

@pytest.mark.alert
def test_alertHandling(playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.on("dialog", lambda dialog: (print(dialog.message), dialog.accept()))
    page.goto("https://rahulshettyacademy.com/AutomationPractise")
    page.wait_for_timeout(2_000)
    page.locator("input[id='confirmbtn']").click(timeout=3_000)
    page.wait_for_timeout(2_000)
    time.sleep(10)

@pytest.mark.iframe
def test_iframeLesson(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractise")
    iframe = page.frame_locator("#courses-iframe")
    iframe.get_by_role("link",name="All Access plan").click()

    expect(iframe.locator("body")).to_contain_text("Happy Subscibers!")

    #check the price of the rice
    #identify the price column
    #identify the rice column
@pytest.mark.riceprice
def test_checkThePriceOfTheRice(page:Page):
    ricePrice = 0
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    page.locator("#page-menu").select_option("20")
    page.wait_for_timeout(3_000)
    rowFoods = page.locator("tr td")
    priceFound = False
    priceColumn = 0
    price = 0
    columnHeadings = page.locator("th[role='columnheader'] span")
    columnPrice = 0
    for columnIndex in range(0,columnHeadings.count()):
        print(f"{columnHeadings.nth(columnIndex)}")
        if columnHeadings.nth(columnIndex).text_content() == "Price":
            if columnIndex < 2:
                priceColumn = columnIndex
                priceFound = True
                break
            else:
                priceColumn = columnIndex - 2
                priceFound = True
                break

    # findRiceRow = page.locator("tr").filter(has_text="Rice")
    # print(f"Found Rice Row: {findRiceRow}")
    # expect(findRiceRow.locator("td").nth(priceColumn)).to_have_text("37")
    #
    # if priceFound == True:
    #     print("Price found")
    #     for index in range(0,rowFoods.count(),3):
    #         if rowFoods.nth(index).text_content() == "Rice":
    #             price = rowFoods.nth(index + 1).text_content()
    #             print(f"Price: {price}")
    #             print("Rice found")
    #             expect(rowFoods.nth(index + 1)).to_contain_text("37")
    # else:
    #     print("Rice not found")





    # count = 0
    # row = 0
    # riceFound = False



    # while riceFound == False:
    #     while count < rowFoods.count() and riceFound == False:
    #          if rowFoods.nth(0) == "Rice":
    #              row += count
    #              riceFound = True
    #              print("Rice Found")
    #              break
    #          elif rowFoods.nth(count) == "Rice":
    #              row += 1
    #              riceFound = True
    #              print("Rice Found")
    #              break
    #          print("No Rice found")
    #          count += 3
    #
    #     page.locator("[aria-label='Next']").click()
    #     rowFoods = page.locator("td tr")
    #     count = 0






    # for count in range(0,rowFoods.count(),3):
    #
    # if page.locator("tr").filter(has_text="Rice Price") > 0:
    #     riceRow = riceRow + 1
    #
    # columnHeaders = page.locator("th[class='columnheader']")
    # for index in range(columnHeaders.count()):
    #     if columnHeaders.nth(index).locator("span") == "Price":
    #         ricePrice = index
    #         print(f"Price column value is {index} ")
    #         break
    #

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
@pytest.mark.hover
def test_mouseOver(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    mouseOver = page.locator("#mousehover")
    mouseOver.scroll_into_view_if_needed()
    mouseOver.hover()
    page.get_by_role("link",name="Top").click()
    time.sleep(4)











