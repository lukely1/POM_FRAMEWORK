from selenium import webdriver
import utilities.CustomLogger as cl


class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome()
            self.log.info("Chrome Driver is initializing")
        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is initializing")
        elif browserName == "firefox":
            driver = webdriver.Firefox()
            self.log.info("FireFox Driver is initializing")

        return driver
