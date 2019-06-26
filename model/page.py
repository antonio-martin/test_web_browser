import time

from selenium.webdriver.firefox.webdriver import WebDriver

from model.element import LogoImage, ResultsLogoImage, ResultsSearchField, ResultsSearchButton, SearchField, \
    SearchButton, ResultsList


class BasePage:
    """Base web page with common functionality"""
    TIMEOUT = 10

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        # Wait for the page to be loaded completely
        waited = 0
        page_state = self.driver.execute_script('return document.readyState;')
        while page_state != 'complete' and waited < self.TIMEOUT:
            time.sleep(1)
            waited += 1


class ResultsPage(BasePage):
    """Duck Duck Go results page"""
    logo = ResultsLogoImage()
    searchField = ResultsSearchField()
    searchButton = ResultsSearchButton()
    results: [] = ResultsList()

    def click_result(self, position: int = 0):
        pass

    def search(self, text: str) -> BasePage:
        self.searchField = text
        self.searchButton

    def click_search(self):
        self.searchButton


class HomePage(BasePage):
    """Duck Duck Go home page"""

    logo = LogoImage()
    searchField = SearchField()
    searchButton = SearchButton()

    def search(self, text: str) -> ResultsPage:
        self.searchField = text
        self.searchButton
        return ResultsPage(driver=self.driver)

    def click_search(self) -> ResultsPage:
        self.searchButton
        return ResultsPage(driver=self.driver)

