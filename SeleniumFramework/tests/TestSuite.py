# 1. Import the files
import unittest
from tests.test_ContactForm import ContactFormTest
from tests.test_EnterText import EnterTextTest
from tests.test_Actions import Actions
from tests.test_DragDrop import DragDropTest
from tests.test_IFrames import IFrames
from tests.test_PopUpWindow import WindowPopup
from tests.test_TablesForm import Table



# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
et = unittest.TestLoader().loadTestsFromTestCase(EnterTextTest)
af = unittest.TestLoader().loadTestsFromTestCase(Actions)
ddt = unittest.TestLoader().loadTestsFromTestCase(DragDropTest)
ifr = unittest.TestLoader().loadTestsFromTestCase(IFrames)
wt = unittest.TestLoader().loadTestsFromTestCase(WindowPopup)
tabf = unittest.TestLoader().loadTestsFromTestCase(Table)



# 3. Create TestSuite
regressionTest = unittest.TestSuite([cf, et, af, ddt, ifr, wt, tabf])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

# Note : All the methods in test files should define in proper run order
