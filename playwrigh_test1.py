import pytest
import allure
from playwright.sync_api import Page, expect, sync_playwright


#page class -- Help you to interact with HtML
#expect-- Validatiom purpose

def test_vwo():
    browser = sync_playwright().start().chromium.launch(headless=False)
    #If you want to open page within same browser by 'context'
    context =browser.new_context()
    page =context.new_page()
    page2=context.new_page()
    page.goto("https://app.vwo.com/#/login")
    page2.goto("https://www.google.com/")
