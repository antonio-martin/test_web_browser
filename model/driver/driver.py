import os
from pathlib import Path

from selenium.webdriver.chrome import webdriver as chromedriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox import webdriver as firefoxdriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver


class DriverFactory:
    chrome_driver = None
    firefox_driver = None
    os.environ["PATH"] += os.pathsep + str(Path(__file__).parent)

    @classmethod
    def get_chrome_driver(cls) -> ChromeWebDriver:
        if cls.chrome_driver is None:
            chrome_options = chromedriver.Options()
            # chrome_options.add_argument("--headless")
            desired_capabilities = {'applicationCacheEnabled': False}
            cls.chrome_driver = chromedriver.WebDriver(options=chrome_options,
                                                       desired_capabilities=desired_capabilities)
            cls.chrome_driver.implicitly_wait(10)  # seconds
        return cls.chrome_driver

    @classmethod
    def get_firefox_driver(cls) -> FirefoxWebDriver:
        if cls.firefox_driver is None:
            firefox_options = firefoxdriver.Options()
            # firefox_options.add_argument("--headless")
            desired_capabilities = {'applicationCacheEnabled': False}
            cls.firefox_driver = chromedriver.WebDriver(options=firefox_options,
                                                        desired_capabilities=desired_capabilities)
            cls.firefox_driver.implicitly_wait(10)  # seconds
        return cls.firefox_driver
