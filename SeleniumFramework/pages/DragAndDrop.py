from base.BasePage import BaseClass
import utilities.CustomLogger as cl


class DragAndDrop(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators  values in Contact form page

    _DragAndDropPage = "DragAndDrop"  # link
    _Drag_ele = "drag" # id
    _Drop_ele = "drop"  # id


    def clickDragAndDropForm(self):
        self.clickOnElement(self._DragAndDropPage, "link")
        cl.allureLogs("Clicked on DragAndDrop Form")

    def verifyDragAndDropPage(self):
        element = self.isElementDisplayed(self._Drag_ele, "id")
        assert element == True
        cl.allureLogs("Verified DragNDrop Form")

    def DragAndDrop(self):
        self.DragNDrop(self._Drag_ele, self._Drop_ele, "id")
        cl.allureLogs("Verified DragNDrop Form")

