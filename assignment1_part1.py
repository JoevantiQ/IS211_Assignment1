# assignment1_part1.py

class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    """
    Returns the count of elements in the list that are divisible by divide.
    :param numbers: List of integers
    :param divide: Integer divisor (default is 2)
    :return: Count of divisible elements
    """
    return sum(1 for num in numbers if num % divide == 0)

def test_list_divide():
    """
    Tests the list_divide function with predefined test cases.
    Raises ListDivideException if any test fails.
    """
    try:
        assert list_divide([1, 2, 3, 4, 5]) == 2
        assert list_divide([2, 4, 6, 8, 10]) == 5
        assert list_divide([30, 54, 63, 98, 100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1, 2, 3, 4, 5], 1) == 5
    except AssertionError:
        raise ListDivideException("Test failed in test_list_divide")

if __name__ == "__main__":
    test_list_divide()
    print("All tests passed successfully!")
