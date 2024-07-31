from selenium.webdriver.common.by import By

from base.BasePage import BaseClass
import utilities.CustomLogger as cl
from selenium.webdriver.common.alert import Alert

class Window(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators  values in Window form page

    _WindowPage = "Windows"  # link
    _WindowText = "section-body"  # text
    _FramePage = "Frame"
    _IFramePage = "section-body"  # class
    _IFrame1 = "f1"  # id
    _IFrame2 = "f2"  # id
    _IFrame3 = "f3"  # id
    _IFrame4 = "f4"  # id
    _PromtAlertBttn = "promtalert"  # name
    _PopUpWind1 = "//*[@id='app']/div/div[3]/section/div[2]/div/form/input[1]"

    def clickWindowsForm(self):
        self.clickOnElement(self._WindowPage, "link")
        cl.allureLogs("Clicked on Window Form")

    def verifyWindowsPage(self):
        element = self.getText(self._WindowText, "class")
        # assert element == True
        #print(element)
        try:
            for el in element:
                assert el == "Click the below button to show the alert box."
                return True
        except AssertionError as msg:
            print('Error')

        cl.allureLogs("Verified Popup Windows")

    def PopUpWindowToIFrame1(self):
        self.clickOnElement(self._PopUpWind1, "xpath")
        # window_handles[1] is a second window
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.maximize_window()
        cl.allureLogs("Clicked on PopUp Window ")

    def CloseCurrentWindow(self):
        # parent = self.driver.current_window_handle
        # uselessWindows = self.driver.window_handles
        # for winId in uselessWindows:
        #     if winId != parent:
        #         self.driver.switch_to.window(winId)
        #         self.driver.close()
        parent = self.driver.current_window_handle
        print(f"This is parent window : {parent}")

        uselessWindows = self.driver.window_handles
        print(
            f"This has the parent window and also the two popup windows : {uselessWindows}")
        self.driver.switch_to.window(uselessWindows[-1])
        self.driver.close()
        self.driver.switch_to.window(uselessWindows[0])
    # def SwitchToIFrame(self, iframe):
    #     # element = self.getWebElement(self, iframe)
    #     ele = self.driver.find_element(By.ID, iframe)
    #     self.driver.switch_to.frame(ele)
    #     #self.driver.switch_to.frame(element)
    #
    # def clickOnPromtAcceptAlertButton(self):
    #     self.clickOnElement(self._PromtAlertBttn, "name")
    #
    #     # Create the object for Alert class
    #     a_button = Alert(self.driver)
    #     a_button.accept()
    #
    # def clickOnPromtDismissAlertButton(self):
    #     self.clickOnElement(self._PromtAlertBttn, "name")
    #
    #     # Create the object for Alert class
    #     a_button = Alert(self.driver)
    #     a_button.dismiss()