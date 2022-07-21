import sqlite3
import time
from playwright.sync_api import sync_playwright
url="https://play.google.com/store/apps"

with sync_playwright()as play:
    browser=play.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto (url)
    page.wait_for_timeout(2000)

    # Connection To Database
    conn = sqlite3.connect("trendingApps.db")
    
    
    ###
        # Trending Free Apps
    ###
    all_apps = page.query_selector_all('.MPNOXb .cXFu1')
    for items in range(len(all_apps)):
        apps_data = all_apps[items].inner_text()
        list_of_apps_data = apps_data.split("\n")

        insertAppData = """INSERT OR IGNORE INTO freeTrendingApps (appId, appName, appCategory, appRatings) VALUES ({}, "{}", "{}", "{}")""".format(items+1, list_of_apps_data[0], list_of_apps_data[1], list_of_apps_data[2])
        curso = conn.cursor()
        curso.execute(insertAppData)
        conn.commit()
    

    ###
        # Trending Grossing Apps
    ###

    page.locator("#ct\|apps_topgrossing").click()
    time.sleep(5)

    all_apps = page.query_selector_all('.MPNOXb .cXFu1')
    for items in range(len(all_apps)):
        apps_data = all_apps[items].inner_text()
        list_of_apps_data = apps_data.split("\n")

        insertAppData = """INSERT OR IGNORE INTO grossingTrendingApps (appId, appName, appCategory, appRatings) VALUES ({}, "{}", "{}", "{}")""".format(items+1, list_of_apps_data[0], list_of_apps_data[1], list_of_apps_data[2])
        curso = conn.cursor()
        curso.execute(insertAppData)
        conn.commit()
    
    ###
        # Trending Paid Apps
    ###

    page.locator("#ct\|apps_topselling_paid").click()
    time.sleep(5)

    all_apps = page.query_selector_all('.MPNOXb .cXFu1')
    for items in range(len(all_apps)):
        apps_data = all_apps[items].inner_text()
        list_of_apps_data = apps_data.split("\n")

        insertAppData = """INSERT OR IGNORE INTO paidTrendingApps (appId, appName, appCategory, appRatings) VALUES ({}, "{}", "{}", "{}")""".format(items+1, list_of_apps_data[0], list_of_apps_data[1], list_of_apps_data[2])
        curso = conn.cursor()
        curso.execute(insertAppData)
        conn.commit()

    # Closing Connection
    conn.close()
    browser.close()

    