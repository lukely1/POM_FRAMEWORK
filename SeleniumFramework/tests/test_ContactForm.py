import unittest
import pytest
import time
from base.BasePage import BaseClass
from pages.ContactFormPage import ContactForm
import utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)
        # self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_formPage(self):
        self.cf.clickContactForm()
        self.cf.verifyFormPage()

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.clickContactForm()
        self.cf.verifyFormPage()
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterMessage()
        self.cf.enterCaptha()
        self.cf.clickOnPostButton()
