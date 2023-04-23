import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_change_gradus():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    temp_change = driver.find_element(By.XPATH, '//*[@id="weather-widget"]/div[1]/div/div/div[1]/div[2]/div[3]')
    time.sleep(10)
    ActionChains(driver).drag_and_drop_by_offset(temp_change, 72, 0).perform()
    time.sleep(10)