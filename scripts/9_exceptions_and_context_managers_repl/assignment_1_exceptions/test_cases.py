import unittest

from code_template import divide


class TestExceptionAssignment(unittest.TestCase):

    def test_divide_integer_result(self):
        self.assertEqual(
            4, divide('16 4'), 'Wrong division result (should be integer value)')

    def test_divide_float_result(self):
        self.assertEqual(
            2.5, divide('5 2'), 'Wrong division result (should be float value)')

    def test_input_trimming(self):
        self.assertEqual(
            5, divide(' 25 5 '), 'Wrong result, you should handle trailing spaces')

    def test_zero_division_error(self):
        self.assertEqual(
            'Error code: division by zero', divide('7 0'), 'Wrong result, you should handle zero division')

    def test_non_numeric_input_error(self):
        self.assertEqual(
            "Error code: invalid literal for int() with base 10: 'ddkg'",
            divide('54 ddkg'),
            'Wrong result, handle non-numeric values in the input'
        )

    def test_extra_values_error(self):
        self.assertEqual(
            'Error code: too many values to unpack (expected 2)',
            divide('5 2 7'),
            'Wrong result, handle extra-parameters in the input'
        )

    def test_missed_values_error(self):
        self.assertEqual(
            'Error code: not enough values to unpack (expected 2, got 1)',
            divide('5'),
            'Wrong result, handle missed parameters in the input'
        )


if __name__ == '__main__':
    unittest.main()
