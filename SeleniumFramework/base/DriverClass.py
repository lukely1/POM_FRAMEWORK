# from urllib import request

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # modified
from webdriver_manager.chrome import ChromeDriverManager # modified
from webdriver_manager.firefox import GeckoDriverManager # modified
import utilities.CustomLogger as cl


class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            options = webdriver.ChromeOptions() # add more option
            # driver = webdriver.Chrome()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            print("Launching chrome browser.........")
            self.log.info("Chrome Driver is initializing")
        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is initializing")
        elif browserName == "firefox":
            driver = webdriver.Firefox()
            self.log.info("FireFox Driver is initializing")

        return driver

    # # @pytest.fixture()
    # def browserName(self):  # This will return the Browser value to setup method
    #     return request.config.getoption("--browser")
