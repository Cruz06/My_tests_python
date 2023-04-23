import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_open():
    #    browser.get('https://suninjuly.github.io/xpath_examples')
    #    time.sleep(5)
    browser.get('http://suninjuly.github.io/cats.html')
    # bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
    view_button = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
    print(view_button)
    assert len(view_button) == 6, "Wrong length"


def test_open_page():
    test_open()