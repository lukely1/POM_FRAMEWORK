import unittest
import pytest
import time
from pages.TablesPage import Tables
from datadriventest.ReadingExcel import ReadingFile


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class Actions(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.tb = Tables(self.driver)
        self.rd = ReadingFile(self)

    @pytest.mark.run(order=1)
    def test_Tables(self):
        self.tb.clickTables()
        self.tb.verifyTablesPage()

    @pytest.mark.run(order=2)
    def test_data_driven(self):
        self.tb.tableRowCount()
        self.tb.tableColumnCount()
        self.tb.verifyTableText("$36,738")
        self.tb.ReadExcelFile()

