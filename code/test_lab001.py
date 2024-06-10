import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

def test_table():
    driver.get("http://43.254.41.220:8080/cau-iums/")
    driver.find_element(By.ID,"login_name").send_keys("cau@gmail.com")
    driver.find_element(By.ID,"login_pass").send_keys("SUSPL@1234")
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@class='lg-btn vldLogin']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"(//a[normalize-space()='LEAVE MANAGEMENT'])[1]").click()
    time.sleep(2)
    # driver.find_element(By.XPATH,"//span[normalize-space()='Calendar Year Master']").click()
    # time.sleep(2)