# assignment1_part1.py

class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    """
    Counts the number of elements in the numbers list that are divisible by divide.

    :param numbers: List of numbers to check.
    :param divide: Integer divisor (default is 2).
    :return: Count of divisible elements.
    """
    if not isinstance(numbers, list) or not isinstance(divide, int):
        raise ListDivideException("Invalid input: 'numbers' must be a list and 'divide' must be an integer.")

    return len([num for num in numbers if num % divide == 0])

def test_list_divide():
    """
    Tests the list_divide function with various cases.
    """
    try:
        assert list_divide([1, 2, 3, 4, 5]) == 2, "Test case 1 failed."
        assert list_divide([2, 4, 6, 8, 10]) == 5, "Test case 2 failed."
        assert list_divide([30, 54, 63, 98, 100], divide=10) == 2, "Test case 3 failed."
        assert list_divide([]) == 0, "Test case 4 failed."
        assert list_divide([1, 2, 3, 4, 5], 1) == 5, "Test case 5 failed."
        print("All tests passed!")
    except AssertionError as e:
        print(e)

# Run the test function if this file is executed directly
if __name__ == "__main__":
    test_list_divide()
