import unittest
import pytest
import time
from pages.EnterTextPage import EnterText
from base.BasePage import BaseClass


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class EnterTextTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.et = EnterText(self.driver)
        #self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=3)
    def test_clickOnLocatorsPage(self):
        self.et.clickOnLocatorsPage()

    @pytest.mark.run(order=4)
    def test_enterDataInEditBox(self):
        self.driver.maximize_window()
        time.sleep(2)
        self.et.enterText()

        self.et.clickOnSubmitButton()
        self.et.clickOnRadiobutton("Button2")

        self.et.clickOnCheckBox("c2")
        self.et.selectOnDropdown(3)

        self.et.clickOnMultiSelect(1)
        self.et.clickOnMultiSelect(2)

        self.et.deselectOnMulti(1)
        self.et.deselectOnMulti(2)

    # @pytest.mark.run(order=5)
    # def test_RadioButtonClick(self):
    #     self.et.clickOnRadiobutton("Button2")

    # @pytest.mark.run(order=6)
    # def test_CheckboxClick(self):
    #     self.et.clickOnCheckBox("c2")



