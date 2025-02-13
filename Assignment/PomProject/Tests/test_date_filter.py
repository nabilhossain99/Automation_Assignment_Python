import pytest
from selenium import webdriver
from Assignment.PomProject.Pages.date_filter_page import DateFilterPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://example.com")  # Replace with actual URL
    yield driver
    driver.quit()

def test_filter_and_submit(driver):
    page = DateFilterPage(driver)
    page.apply_date_filter("2024-02-13")
    page.select_all_results()
    page.submit_results()
