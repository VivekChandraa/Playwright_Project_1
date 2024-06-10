import time

from playwright.sync_api import Page, expect,sync_playwright
def test_app():
    browser = sync_playwright().start().chromium.launch(headless=False)
    page =browser.new_page()
    # page.goto("https://katalon-demo-cura.herokuapp.com/")
    # page.locator("//a[@id='btn-make-appointment']").click()
    # page.get_by_placeholder("Username").click()
    # page.get_by_placeholder("Username").fill("John Doe")
    # page.locator("//a[@id='btn-make-appointment']").click()
    page.goto("https://katalon-demo-cura.herokuapp.com/")
    page.get_by_role("link", name="Make Appointment").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("John Doe")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("ThisIsNotAPassword")
    page.get_by_role("button", name="Login").click()
    page.get


