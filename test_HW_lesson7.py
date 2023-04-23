from itertools import count
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_open_page(driver):
    driver.get("https://openweathermap.org/marketplace")
    driver.maximize_window()
    assert "https://openweathermap.org/marketplace" in driver.current_url


def test_check_page_title(driver):
    driver.get("https://openweathermap.org/marketplace")
    driver.maximize_window()
    assert driver.title == 'Marketplace: History Bulk, History Forecast Bulk, Historical Weather Data by State for all ZIP codes, USA - OpenWeather'


def test_find_element(driver):
    driver.get('https://openweathermap.org/marketplace')
    search_block2 = driver.find_element(By.XPATH, '//*[@id="historical_data_archives"]')
    expected_block2 = "Historical Data Archives"
    assert search_block2.text == expected_block2


def test_find_element_long(driver):
    driver.get('https://openweathermap.org/marketplace')
    search_block1 = driver.find_element(By.XPATH, '//*[@id="custom_weather_products"]')
    expected_block1 = 'Custom Weather Products\nOpenWeatherMap provides access to 40-year historical weather data for any location. Get various weather parameters, such as temperature, precipitation, wind and many more.'
    assert search_block1.text == expected_block1


#def test_count_buttons(driver):
#    driver.get('https://openweathermap.org/marketplace')
#    search_button = driver.find_element(By.XPATH, '//div/*[@class="button-round dark"]')
#    expected_count = 3
#    assert len(search_button) == expected_count, "Wrong length"

def test_text_on_buttons(driver):
    driver.get('https://openweathermap.org/marketplace')
    search_button = driver.find_element(By.XPATH, '//div/*[@class="button-round dark"]')
    expected_text = "Place order"
    assert search_button.text == expected_text