from selenium.webdriver.common.by import By

from base.BasePage import BaseClass
import utilities.CustomLogger as cl
from selenium.webdriver.common.alert import Alert

class Frame(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators  values in Contact form page

    _FramePage = "Frame"  # link
    _IFramePage = "section-body"  # class
    _IFrame1 = "f1"  # id
    _IFrame2 = "f2"  # id
    _IFrame3 = "f3"  # id
    _IFrame4 = "f4"  # id
    _PromtAlertBttn = "promtalert"  # name

    def clickIFrameForm(self):
        self.clickOnElement(self._FramePage, "link")
        cl.allureLogs("Clicked on Frame Form")

    def verifyIFramesPage(self):
        element = self.isElementDisplayed(self._IFramePage, "class")
        assert element == True
        cl.allureLogs("Verified IFrames Form")

    def SwitchToIFrame(self, iframe):
        # element = self.getWebElement(self, iframe)
        ele = self.driver.find_element(By.ID, iframe)
        self.driver.switch_to.frame(ele)
        #self.driver.switch_to.frame(element)

    def clickOnPromtAcceptAlertButton(self):
        self.clickOnElement(self._PromtAlertBttn, "name")

        # Create the object for Alert class
        a_button = Alert(self.driver)
        a_button.accept()

    def clickOnPromtDismissAlertButton(self):
        self.clickOnElement(self._PromtAlertBttn, "name")

        # Create the object for Alert class
        a_button = Alert(self.driver)
        a_button.dismiss()



