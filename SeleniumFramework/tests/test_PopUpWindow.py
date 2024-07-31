import unittest
import pytest
import time
from pages.WindowPage import Window
from pages.FramePage import Frame


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class WindowPopup(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.wd = Window(self.driver)
        self.ifr = Frame(self.driver)

    @pytest.mark.run(order=1)
    def test_Window(self):
        self.wd.clickWindowsForm()
        self.wd.verifyWindowsPage()

        # Click on Popup 1
        self.wd.PopUpWindowToIFrame1()

    @pytest.mark.run(order=2)
    def test_FramePage1(self):
        self.ifr.clickIFrameForm()
        self.ifr.verifyIFramesPage()
        self.ifr.SwitchToIFrame("f1")
        self.ifr.clickOnPromtAcceptAlertButton()

        # Switching back to normal content page from frame
        self.driver.switch_to.default_content()

    @pytest.mark.run(order=3)
    def test_FramePage2(self):
        self.ifr.clickIFrameForm()
        self.ifr.verifyIFramesPage()
        self.ifr.SwitchToIFrame("f2")
        self.ifr.clickOnPromtDismissAlertButton()

        # Switching back to normal content page from frame
        self.driver.switch_to.default_content()

    @pytest.mark.run(order=4)
    def test_FramePage3(self):
        self.ifr.clickIFrameForm()
        self.ifr.verifyIFramesPage()
        self.ifr.SwitchToIFrame("f3")
        self.ifr.clickOnPromtAcceptAlertButton()

        # Switching back to normal content page from frame
        self.driver.switch_to.default_content()

    @pytest.mark.run(order=5)
    def test_FramePage4(self):
        self.ifr.clickIFrameForm()
        self.ifr.verifyIFramesPage()
        self.ifr.SwitchToIFrame("f4")
        #self.ifr.clickOnPromtDismissAlertButton()

        # Switching back to normal content page from frame
        self.driver.switch_to.default_content()
        self.ifr.clickOnPromtDismissAlertButton()
        # self.wd.CloseCurrentWindow()

