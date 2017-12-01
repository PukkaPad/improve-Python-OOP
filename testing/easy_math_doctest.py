'''
Module showing how doctests can be included with source code
Each '>>>' line is run as if in a python shell, and counts as a test.
The next line, if not '>>>' is the expected output of the previous line.
If anything doesn't match exactly (including trailing spaces), the test fails.
'''

def multiply(a, b):
    """
    >>> multiply (4, 3)
    12
    >>> multiply ("m", 4)
    'mmmm'
    """
    return a * b

# python3 -m doctest easy_math_doctest.py
# python3 -m doctest -v easy_math_doctest.py