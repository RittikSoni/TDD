import re
import unittest

def add(numbers):
    """
    Adds up numbers provided in a string.

    The input string can contain numbers separated by commas or new lines.
    Custom delimiters can be specified in the format "//[delimiter]\n[numbers]".

    Args:
        numbers (str): A string containing numbers separated by delimiters.

    Returns:
        int: The sum of the numbers.

    Raises:
        ValueError: If the input string contains negative numbers.
    """
    if not numbers:
        return 0
    
    delimiter = ",|\n"
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]
    
    num_list = re.split(delimiter, numbers)
    
    total = 0
    negatives = []
    for num in num_list:
        if num:
            n = int(num)
            if n < 0:
                negatives.append(n)
            total += n
    
    if negatives:
        raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
    
    return total

class TestStringCalculator(unittest.TestCase):
    """
    Unit tests for the String Calculator.
    """

    def test_empty_string(self):
        """
        Test that an empty string returns 0.
        """
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        """
        Test that a single number returns itself.
        """
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        """
        Test that two numbers separated by a comma return their sum.
        """
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers(self):
        """
        Test that multiple numbers separated by commas return their sum.
        """
        self.assertEqual(add("1,2,3"), 6)

    def test_new_lines_between_numbers(self):
        """
        Test that new lines between numbers are handled correctly.
        """
        self.assertEqual(add("1\n2,3"), 6)

    def test_different_delimiters(self):
        """
        Test that custom delimiters are supported.
        """
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        """
        Test that negative numbers raise an exception with all negatives listed.
        """
        with self.assertRaises(ValueError) as context:
            add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -4")

if __name__ == "__main__":
    unittest.main()
