from base.BasePage import BaseClass
import utilities.CustomLogger as cl
import time
from selenium.webdriver.support.select import Select

class EnterText(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact form
    _locatorsPage = "Locators" # link
    _enterTextEditBox = "user_input"  # id
    _submitButton = "submitbutton"  # id
    _radioButton = "radio"  # name
    #_radioValue = "Button2"
    _checkboxButton = "checkbox"
    _dropDown = "dropdown"
    _multiSelect = "multiselect"

    def clickOnLocatorsPage(self):
        self.clickOnElement(self._locatorsPage, "link")

    def enterText(self):
        self.sendText("Code2Lead", self._enterTextEditBox, "id")
        cl.allureLogs("Entered Text in Edit Box")

    def clickOnSubmitButton(self):
        self.clickOnElement(self._submitButton, "id")

    def clickOnRadiobutton(self, btnval):
        elr = self.radioButtons(self._radioButton, "name")
        # 2. Using for loop iterate the list object and click on required option
        for rbutton in elr:
            rbutton_t = rbutton.get_attribute("value")
            print(rbutton_t)
            if rbutton_t == btnval:
                rbutton.click()
                print("Is Selected : ", rbutton.is_selected())
                break

    def clickOnCheckBox(self, btnval):
        elb = self.checkBoxes(self._checkboxButton, "name")
        # 2. Using for loop iterate the list object and click on required option
        for cbutton in elb:
            cbutton_t = cbutton.get_attribute("value")
            print(cbutton_t)
            if cbutton_t == btnval and cbutton.is_selected():
                # cbutton.click()
                print("Is Selected : ", cbutton.is_selected())
                break
            elif cbutton_t == btnval:
                cbutton.click()
                print("Is Selected : ", cbutton.is_selected())
                break

    def selectOnDropdown(self, opt):
        el_drop = self.dropDown(self._dropDown, "id")
        # Create the object for Select class
        dd_options = Select(el_drop)
        # List the values in Drop Down
        dd_v = dd_options.options
        for dd_values in dd_v:
            print(dd_values.text)

        # Click by Index
        dd_options.select_by_index(opt)
        time.sleep(2)

        #
        # # Click by Value
        # dd_options.select_by_value("OptionThree")
        # time.sleep(2)
        #
        # # Click by Text
        # dd_options.select_by_visible_text("Option5")

    def clickOnMultiSelect(self, ms_opt):
        el_ms = self.multiSelect(self._multiSelect, "id")

        # Create the object for Select class
        ms_options = Select(el_ms)

        # List the values in Multi Select
        ms_v = ms_options.options
        for ms_value in ms_v:
            print(ms_value.text)

        # Click by Index
        ms_options.select_by_index(ms_opt)
        # # Click by Value
        #ms_options.select_by_value(ms_opt)
        # # Click by Text
        # ms_options.select_by_visible_text("mOption3")

        time.sleep(2)

        # deselect_by_index
        # ms_options.deselect_by_index(ms_opt)
        # time.sleep(2)

        # # deselect_by_value
        # ms_options.deselect_by_value("mOptionTWo")
        # time.sleep(2)
        #
        # # deselect_by_visible_text
        # ms_options.deselect_by_visible_text("mOption3")
        # time.sleep(2)

    def deselectOnMulti(self, ms_opt):
        el_ms = self.multiSelect(self._multiSelect, "id")

        # Create the object for Select class
        ms_options = Select(el_ms)

        # List the values in Multi Select
        ms_v = ms_options.options
        for ms_value in ms_v:
            print(ms_value.text)

        time.sleep(2)

        # deselect_by_index
        ms_options.deselect_by_index(ms_opt)
        time.sleep(2)