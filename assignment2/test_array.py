"""
Tests for our array class
"""

from array_class import Array

# 1D tests (Task 4)


def test_str_1d():
    arr1 = Array((5,), 0, 5, 3, 2, 1)
    assert str(arr1) == "[0, 5, 3, 2, 1]"

def test_add_1d():
    arr1 = Array((3,), -3, -10, 0)
    arr2 = Array((2,), 5, -5)
    arr3 = Array((3,), 7, 15, 20)
    assert 10 + arr1 == Array((3,), 7, 0, 10)
    assert 11 + arr1 == Array((3,), 8, 1, 11)
    assert arr2+2 == 2+arr2
    assert arr1 + arr3 == Array((3,), 4, 5, 20)

def test_sub_1d():
    arr1 = Array((3,), -3, -10, 0)
    arr2 = Array((2,), 5, -5)
    arr3 = Array((3,), 5, 7, 13)
    assert 10 - arr1 == Array((3,), 13, 20, 10)
    assert 11 - arr1 == Array((3,), 14, 21, 11)
    assert arr2-5 == Array((2,), 0, -10)
    assert arr3-arr1 == Array((3,), 8, 17, 13)

def test_mul_1d():
    arr1 = Array((3,), -3, -10, 0)
    arr2 = Array((2,), 5, -5)
    arr3 = Array((3,), 7, 15, 20)
    assert 10 * arr1 == Array((3,), -30, -100, 0)
    assert 11 * arr1 == Array((3,), -33, -110, 0)
    assert arr2*2 == 2*arr2
    assert arr1 * arr3 == Array((3,), -21, -150, 0)

def test_eq_1d():
    arr1 = Array((5,), 1.0, 2.5, 3.7, 0.0, -3.0)
    arr2 = Array((5,), 1.0, 2.5, 3.7, 0.0, -3.0)
    arr3 = Array((5,), 1.0, 2.0, 3.0, 0.0, -3.0)
    arr4 = Array((5,), 1, 2, 3, 0, -3)
    arr5 = Array((5,), 1, 2, 3, 0, -3)
    assert arr1 == arr2
    assert arr1 != arr3
    assert arr3 != arr4
    assert arr4 == arr5

def test_same_1d():
    arr1 = Array((7,), 1, 2, 3, 4, 5, 6, 7)
    arr2 = Array((7,), 7, 6, 5, 4, 3, 2, 1)
    assert arr1.is_equal(arr2) == Array((7,), False, False, False, True, False, False, False)
    arr3 = Array((7,), 1, 2, 3, 4, 5, 6, 8)
    assert arr3.is_equal(arr1) == Array((7,), True, True, True, True, True, True, False)

def test_smallest_1d():
    arr1 = Array((5,), -10, -15, 0, 200, -100)
    arr2 = Array((4,), -5.0, 5.0, 10.0, -13.0)
    assert arr1.min_element() == -100.0
    assert arr2.min_element() == -13.0

def test_mean_1d():
    arr1 = Array((4,), 0, 10, 20, 20)
    arr2 = Array((3,), 5.0, 6.0, 10.0)
    assert arr1.mean_element() == 12.5
    assert arr2.mean_element() == 7.0


# 2D tests (Task 6)


def test_add_2d():
    pass


def test_mult_2d():
    pass


def test_same_2d():
    pass


def test_mean_2d():
    pass


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    '''
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
    '''