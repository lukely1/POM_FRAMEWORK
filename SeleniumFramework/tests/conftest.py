import pytest
from base.BasePage import BaseClass
from base.DriverClass import WebDriverClass
import time


# When parameter scope = "class"
# multiple test cases in class will get executed and will only call driver function once.
@pytest.yield_fixture(scope='class')
#def beforeClass(request):
def beforeClass(request, browser):
    print('Before Class')
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver(browser)
    # driver = driver1.getWebDriver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template")
    # bp.launchWebPage("http://www.dummypoint.com/Form.html", "Selenium Template")
    driver.maximize_window()
    time.sleep(2)
    #  it is clear that we are assigning driver value for the invoke test function.
    #  So, before opening an URL we need a browser which is driver
    #  and it is assigned using fixture with scope on class level.
    #  request.cls.driver = driver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


# example command run test with option select browser pytest -s -v .\test_ContactForm.py --browser firefox (chrome,...)
def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture(scope="session")
# This will return the Browser value to setup method,
# example command run test with option select browser pytest -s -v .\test_ContactForm.py --browser firefox (chrome,...)
def browser(request):

    return request.config.getoption("--browser")

@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
