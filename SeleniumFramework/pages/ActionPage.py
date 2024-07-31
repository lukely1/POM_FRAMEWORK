from base.BasePage import BaseClass
import utilities.CustomLogger as cl
import time


class Action(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact form
    _locatorsPage = "Actions"  # link
    _enterTextEditBox = "user_input"  # id
    _submitButton = "submitbutton"  # id
    #_radioButton = "radio"  # name
    # _radioValue = "Button2"
    #_checkboxButton = "checkbox"
    #_dropDown = "dropdown"
    #_multiSelect = "multiselect"

    def clickOnActionPage(self):
        self.clickOnElement(self._locatorsPage, "link")

    def enterText(self, txt):
        self.sendText(txt, self._enterTextEditBox, "id")
        cl.allureLogs("Entered Text in Edit Box")

    def clickOnSubmitButton(self):
        self.clickOnElement(self._submitButton, "id")


