import pytest
import allure
from playwright.sync_api import Page, expect, sync_playwright
def test_vwo():
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://app.vwo.com/#/login")
