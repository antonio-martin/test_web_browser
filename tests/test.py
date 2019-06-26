import pytest

from model.driver.driver import DriverFactory
from model.page import HomePage, ResultsPage


@pytest.fixture(scope="session", autouse=True)
def setup():
    driver = DriverFactory.get_chrome_driver()
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def home_page(setup):
    url = 'https://duckduckgo.com'
    setup.get(url)
    home_page: HomePage = HomePage(driver=setup)
    return home_page


def test_search_homepage(home_page: HomePage):
    results_page: ResultsPage = home_page.search(text='Madrid')
    results = results_page.results
    assert len(results) > 5, 'Did not found enough results'


def test_search_from_results_page(home_page: HomePage):
    results_page: ResultsPage = home_page.search('hi')
    results_before = results_page.results
    first_result_text_before = results_before[0].text
    results_page.search(text='Malaga')
    results_after = results_page.results
    assert len(results_after) > 5
    first_result_text_after = results_page.results[0].text
    assert first_result_text_before != first_result_text_after


