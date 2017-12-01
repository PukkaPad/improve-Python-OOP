
from testing.easy_math import multiply

def test_multiply_4_3():
    assert multiply (4, 3) == 12

def test_string_multiply_m_4():
    assert multiply ("m", 4) == "mmmm"

# nosetests test_easy_math_nose
# nosetests -v test_easy_math_nose