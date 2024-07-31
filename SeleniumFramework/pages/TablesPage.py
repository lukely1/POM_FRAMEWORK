from base.BasePage import BaseClass
import utilities.CustomLogger as cl
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datadriventest import XLutils
import pandas as pd


class Tables(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact form
    _locatorsPage = "Tables"  # link
    _Tablespage = "card-title"  # class
    _submitButton = "submitbutton"  # id

    # _tableRows = "//*[@id='tt']/div/table/tbody/tr"
    # _tableColumns = "//*[@id='tt']/div/table/thead/tr/th"

    def clickTables(self):
        self.clickOnElement(self._locatorsPage, "link")
        cl.allureLogs("Clicked on Contact Form")

    def verifyTablesPage(self):
        element = self.isElementDisplayed(self._Tablespage, "class")
        assert element == True
        cl.allureLogs("Verified Tables displayed")

    def tableRowCount(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        rows = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//*[@id='tt']/div/table/tbody/tr")))

        #rows = self.driver.find_elements(By.XPATH, "//*[@id='tt']/div/table/tbody/tr")
        number_of_rows = len(rows)
        print("The Rows  # :", number_of_rows)

    def tableColumnCount(self):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        cols = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//*[@id='tt']/div/table/thead/tr/th")))
        # cols = self.driver.find_elements(By.XPATH, "//*[@id='tt']/div/table/thead/tr/th")
        number_of_cols = len(cols)
        print("The Columns # :", number_of_cols)

        # to get the data from 2nd row and 2nd column directly
        # val = driver.find_elements_by_xpath("//table/tbody/tr[2]/td[2]").text

    def verifyTableText(self, val):
        # datalist = []
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
        data_table = [x.text for x in
                      wait.until(ec.presence_of_all_elements_located((By.XPATH, "//*[@id='tt']/div/table/tbody/tr")))]
        print(data_table)
        # list(filter(lambda y: val in y, datalist))

        if any(val in dt for dt in data_table):
            print('Found Text : ' + val + ' in the table - PASS')
            assert True
        else:
            print('Not Found Text: ' + val + ' in the table - Fail')
            assert False

        # for data in data_table:
        #     if val in data:
        #         print('Found Value in the table - PASS')
        #         assert True
        #     else:
        #         print('Not Found Value in the table - Fail')
        #         assert False
        #     print(data_table)

        # for data in data_table:
        #     if data == val:
        #         assert True
        #     print(val.text)
        # cols = self.driver.find_elements(By.XPATH, "//*[@id='tt']/div/table/thead/tr/th")

        # print("The Columns # :", cols)

        # to get the data from 2nd row and 2nd column directly
        # val = driver.find_elements_by_xpath("//table/tbody/tr[2]/td[2]").text

    def ReadExcelFile(self):
        file = "C:/Users/lukel/Desktop/appium_test/Selenium_Data.xlsx"
        rows = XLutils.getRowCount(file, "Name")

        # iterating and reading data from spreadsheet excel
        for r in range(2, rows + 1):
            # reading data from spreadsheet excel
            name = XLutils.readData(file, "Name", r, columnno=1)
            country = XLutils.readData(file, "Name", r, columnno=2)
            cty = XLutils.readData(file, "Name", r, 3)
            salary = XLutils.readData(file, "Name", r, 4)
            dat_excel = [name, country, cty, str(salary)]
            # print(dat_excel)

            # get data from table application to verify with data from spreadsheet.
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

            data_table = [x.text for x in
                          wait.until(
                              ec.presence_of_all_elements_located((By.XPATH, "//*[@id='tt']/div/table/tbody/tr")))]
            # print(data_table)

            # iterating and reading data from spreadsheet excel verified with data table from application
            for x in dat_excel:
                # print(x)
                if any(x in data_table for data_table in dat_excel):
                    print('Found Text : ' + x + ' in the spreadsheet row number : ' + str(r), '- PASS')
                    assert True
                else:
                    print('Not Found Text: ' + x + ' in the spreadsheet row number : ' + str(r), '- Fail')
                    assert False
