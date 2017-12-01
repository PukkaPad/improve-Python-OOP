# unittest
import unittest
from prime_function import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for prime_function.py"""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_four_isnot_prime(self):
        """Is 4 determined as non-prime? """
        self.assertFalse(is_prime(4), msg = '4 is not a prime number!')

    def test_negative_number(self):
        """Is a negative number correctly determined as non-prime?"""
        for num in range (-1, -10, -1):
            self.assertFalse(is_prime(num), msg='{} should not be determined to be prime'.format(num))


if __name__ == '__main__':
    unittest.main()

# run:
# python3 test_prime_function.py
# or
# python 2.7.x
# py.test -l test_prime_function.py
# python 3.6.x
# python3 -m pytest test_prime_function.py
# nosetests -v test_prime_function.py