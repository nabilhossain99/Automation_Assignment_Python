from selenium.webdriver.common.by import By
from Assignment.PomProject.Pages.base_page import BasePage

class DateFilterPage(BasePage):
    DATE_INPUT = (By.ID, "date-filter")  # Example locator
    SEARCH_BUTTON = (By.ID, "search-btn")
    RESULTS = (By.CLASS_NAME, "result-item")
    NEXT_BUTTON = (By.ID, "next-page")
    SUBMIT_BUTTON = (By.ID, "submit")

    def apply_date_filter(self, date):
        self.type(self.DATE_INPUT, date)
        self.click(self.SEARCH_BUTTON)

    def select_all_results(self):
        while True:
            results = self.driver.find_elements(*self.RESULTS)
            for result in results:
                result.click()  # Assuming checkboxes
            try:
                next_button = self.driver.find_element(*self.NEXT_BUTTON)
                if next_button.is_enabled():
                    next_button.click()
                else:
                    break
            except:
                break

    def submit_results(self):
        self.click(self.SUBMIT_BUTTON)
