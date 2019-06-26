from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from model.locator import HomePageLocators, ResultsPageLocators


class BaseElement(object):
    """Base element with common functionality"""
    TIMEOUT = 60

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        global driver
        driver = obj.driver
        element = WebDriverWait(driver, self.TIMEOUT).until(
            lambda driver: driver.find_element(*self.LOCATOR))
        return element


class IterableElement(BaseElement):
    """Iterable element as lists"""

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        global driver
        global elements
        driver = obj.driver
        elements = WebDriverWait(driver, self.TIMEOUT).until(
            lambda driver: driver.find_elements(*self.LOCATOR))
        return elements

    def len(self):
        return len(elements)


class FieldElement(BaseElement):
    def __get__(self, obj, owner):
        element = super().__get__(obj, owner)
        return element.get_attribute("value")

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, self.TIMEOUT).until(
            lambda driver: driver.find_element(*self.LOCATOR))
        element = WebDriverWait(driver, self.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(self.LOCATOR))
        element.clear()
        element.send_keys(value)


class ClickableElement(BaseElement):
    def __get__(self, obj, owner):
        super().__get__(obj, owner)
        driver = obj.driver
        expected_conditions
        element = WebDriverWait(driver, self.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(self.LOCATOR))
        element.click()
        return self

#########################
#       HOME PAGE       #
#########################


class LogoImage(ClickableElement):
    LOCATOR = HomePageLocators.LOGO


class SearchField(FieldElement):
    LOCATOR = HomePageLocators.SEARCH_FIELD


class SearchButton(ClickableElement):
    LOCATOR = HomePageLocators.SEARCH_BUTTON


#########################
#     RESULTS PAGE      #
#########################


class ResultsLogoImage(ClickableElement):
    LOCATOR = ResultsPageLocators.LOGO


class ResultsSearchField(FieldElement):
    LOCATOR = ResultsPageLocators.SEARCH_FIELD


class ResultsSearchButton(ClickableElement):
    LOCATOR = ResultsPageLocators.SEARCH_BUTTON


class ResultsList(IterableElement):
    LOCATOR = ResultsPageLocators.RESULTS





