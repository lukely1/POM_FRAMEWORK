import unittest
import pytest
import time
from pages.FramePage import Frame
from base.BasePage import BaseClass

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class IFrames(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ifr = Frame(self.driver)

    @pytest.mark.run(order=1)
    def test_FramePage1(self):
        self.ifr.clickIFrameForm()
        self.ifr.verifyIFramesPage()
        self.ifr.SwitchToIFrame("f1")
        self.ifr.clickOnPromtAcceptAlertButton()

        # Switching back to normal content page from frame
        self.driver.switch_to.default_content()

    @pytest.mark.run(order=2)
    def test_FramePage2(self):
        self.ifr.clickIFrameForm()
        self.ifr.verifyIFramesPage()
        self.ifr.SwitchToIFrame("f2")
        self.ifr.clickOnPromtDismissAlertButton()

        # Switching back to normal content page from frame
        self.driver.switch_to.default_content()

    @pytest.mark.run(order=3)
    def test_FramePage3(self):
        self.ifr.clickIFrameForm()
        self.ifr.verifyIFramesPage()
        self.ifr.SwitchToIFrame("f3")
        self.ifr.clickOnPromtAcceptAlertButton()

        # Switching back to normal content page from frame
        self.driver.switch_to.default_content()

    @pytest.mark.run(order=4)
    def test_FramePage4(self):
        self.ifr.clickIFrameForm()
        self.ifr.verifyIFramesPage()
        self.ifr.SwitchToIFrame("f4")
        #self.ifr.clickOnPromtDismissAlertButton()

        # Switching back to normal content page from frame
        self.driver.switch_to.default_content()
        self.ifr.clickOnPromtDismissAlertButton()




