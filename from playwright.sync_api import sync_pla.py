from re import A
from playwright.sync_api import sync_playwright
url="https://www.saucedemo.com/"
with sync_playwright()as play:
    browser=play.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto (url)
    page.fill("#user-name","standard_user")
    page.fill("[name=password]","secret_sauce")
    page.locator("#login-button").click()
    All_products=page.query_selector_all(".inventory_item")
    for items in All_products:
        name= items.query_selector(".inventory_item_name").inner_text()
        Description= items.query_selector(".inventory_item_desc").inner_text()
        price= items.query_selector(".inventory_item_price").inner_text()
        print("Name:",name)
        print("Description:",Description)
        print("Price:",price)
        print("*********************************************")
    page.wait_for_timeout(2000)
    browser.close()