import unittest
import pytest
import time
from pages.DragAndDrop import DragAndDrop


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class DragDropTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.dnd = DragAndDrop(self.driver)
        #self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_dragNdropPage(self):
        self.dnd.clickDragAndDropForm()
        self.dnd.verifyDragAndDropPage()

    @pytest.mark.run(order=2)
    def test_dragNdrop(self):
        self.dnd.clickDragAndDropForm()
        self.dnd.DragAndDrop()