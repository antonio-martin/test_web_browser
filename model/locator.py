from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGO = (By.ID, 'logo_homepage_link')
    SEARCH_FIELD = (By.ID, 'search_form_input_homepage')
    SEARCH_BUTTON = (By.ID, 'search_button_homepage')


class ResultsPageLocators:
    LOGO = (By.XPATH, '//div[@class="header__search-wrap")]/a/span')
    SEARCH_FIELD = (By.ID, 'search_form_input')
    SEARCH_BUTTON = (By.ID, 'search_button')
    RESULTS = (By.XPATH, '//div[@id="links"]/div[contains(@id, "r1-")]')
