import re
from playwright.sync_api import Page, expect,sync_playwright


def test_example():
    browser=sync_playwright().start().chromium.launch(headless=False)
    page=browser.new_page()

    page.goto("http://43.254.41.220:8080/cau-iums/")
    page.get_by_placeholder("Enter UserID").click()
    page.get_by_placeholder("Enter UserID").fill("cau@gmail.com")
    page.get_by_placeholder("Enter UserID").press("Tab")
    page.get_by_placeholder("Enter Password").fill("SUSPL@1234")
    page.get_by_role("button", name="Login to Continue...").click()
    page.get_by_role("link", name="HRMS ").click()
    page.get_by_role("link", name=" Employee Master ").click()
    page.get_by_role("link", name=" Create and Manage Employee").click()
    page.frame_locator("#child-iframe").locator("#Xlocation").select_option("LC0012")
    page.frame_locator("#child-iframe").locator("#Xddo").select_option("DDO001")
    page.frame_locator("#child-iframe").get_by_role("button", name="Search").click()
    page.frame_locator("#child-iframe").frame_locator("iframe[name=\"btmfrmCreateManageEmpD\"]").locator("#EDIT_RECORD_1").click()
    page.frame_locator("#child-iframe").frame_locator("iframe[name=\"btmfrmCreateManageEmpD\"]").locator("#EDIT_RECORD_1").click()
    page.frame_locator("#child-iframe").frame_locator("iframe[name=\"btmfrmCreateManageEmpD\"]").locator("#EDIT_RECORD_1").click()
    page.frame_locator("#child-iframe").frame_locator("iframe[name=\"btmfrmCreateManageEmpD\"]").locator("#EDIT_RECORD_1").click()
    page.frame_locator("#child-iframe").frame_locator("iframe[name=\"btmfrmCreateManageEmpD\"]").locator("#EDIT_RECORD_1").click()
    page.frame_locator("#child-iframe").frame_locator("iframe[name=\"btmfrmCreateManageEmpD\"]").get_by_role("gridcell", name=" Edit").click()
    page.frame_locator("#child-iframe").locator("#tab_info").get_by_text("Salary Structure").click()
    page.frame_locator("#child-iframe").get_by_role("button", name="Update").click()
