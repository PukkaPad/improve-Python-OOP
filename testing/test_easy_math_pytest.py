from easy_math import multiply

def setup_module(module):
    print ("\nsetup_module: %s \n" % module.__name__)

def teardown_module(module):
    print ("\nteardown_module: %s \n" % module.__name__)

def setup_function(function):
    print ("\nsetup_function: %s \n" % function.__name__)

def teardown_function(function):
    print ("\nteardown_function: %s \n" % function.__name__)


def test_multiply_4_3():
    print ('test_numbers_4_3  <============================ actual test code')
    assert multiply (4, 3) == 12

def test_string_multiply_m_4():
    print ('test_strings_m_4  <============================ actual test code')
    assert multiply('m', 4) == 'mmmm'

# python3 -m pytest test_easy_math_pytest.py
# python3 -m pytest -v test_easy_math_pytest.py
# python3 -m pytest -s test_easy_math_pytest.py