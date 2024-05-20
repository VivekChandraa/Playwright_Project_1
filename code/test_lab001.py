from playwright.sync_api import Page, expect, sync_playwright

def test_cau():
    browser=sync_playwright().start().chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("http://43.254.41.220:8080/cau-iums/")