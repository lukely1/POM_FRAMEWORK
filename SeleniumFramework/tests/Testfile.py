from base.DriverClass import WebDriverClass
import utilities.CustomLogger as cl
from base.BasePage import BaseClass
import time

wd = WebDriverClass()

driver = wd.getWebDriver("chrome")
bp = BaseClass(driver)

bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")
#el =bp.getWebElement("user_input", "id")
bp.sendText("code2lead", "user_input", "id")
#bp.clickOnElement("Form", "link")

#driver.maximize_window()
time.sleep(2)
driver.quit()