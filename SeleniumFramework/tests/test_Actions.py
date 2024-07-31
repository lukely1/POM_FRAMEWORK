import unittest
import pytest
import time
from pages.ActionPage import Action


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class Actions(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.atc = Action(self.driver)

    @pytest.mark.run(order=1)
    def test_Action(self):
        self.atc.clickOnActionPage()

        # Click on Popup 1
        self.atc.enterText("test")
        self.atc.clickOnSubmitButton()