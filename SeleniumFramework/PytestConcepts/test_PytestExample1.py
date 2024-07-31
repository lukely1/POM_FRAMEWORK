"""
Install pytest using pip (pip3 install pytest)

##### Naming Conventions of PyTest ###########
1) File name should start with "test_PytestExample1.py"
2) Method name should start with "test_methodA"

######## 3 Ways of executing the code in pytest #############

py.test -v -s files_path    # run all tests in specific files_path
py.test -v -s test_mod.py py.  # run tests in module or in test file
py.test -v -s test_module.py::test_method  # only run test_method in test_module.py

-v : verbose (verbose is an argument which is used to report more information about an operation in your program )
-s : to print statements
"""

def test_methodA():
    print("This is method A")

def test_methodB():
    print("This is method B")