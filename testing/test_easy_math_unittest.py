import unittest
from easy_math import multiply

class TestEasyMath(unittest.TestCase):

    def test_multiply_4_3(self):
        #print ('test_numbers_4_3  <============================ actual test code')
        self.assertEqual( multiply (4, 3), 12)

    def test_string_multiply_m_4(self):
        #print ('test_strings_m_4  <============================ actual test code')
        self.assertEqual( multiply ("m", 4), "mmmm")

if __name__ == '__main__':
    unittest.main()


# python3 test_easy_math_unittest.py
# python3 -m unittest discover -v test_easy_math_unittest