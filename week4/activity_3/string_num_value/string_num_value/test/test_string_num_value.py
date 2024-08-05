import unittest
from app.string_num_value import StringNumValue


class TestStringNumValue(unittest.TestCase):
    """
    A simple test suite for the StringNumValue class. Read the docstring of
    the class to determine the rules. You can use the rules to write useful
    tests.

    Note that you can provide descriptive test case names (i.e., the method
    names below) so you don't also have to add comments.

    Try to understand this little project with the existing unit tests. Then
    try to add a few new test cases. It's okay if you can think of new
    functionality for the class (which you then also need to develop).
    """
    def setUp(self) -> None:
        """
        Prepare the test fixture. We can now reuse the "unit under test"
        across multiple tests, bearing in mind it will be initialised
        every time.
        """
        self.uut = StringNumValue('')

    def test_unit_under_test_is_the_right_type(self):
        self.assertIsInstance(self.uut, StringNumValue)

    def test_empty_string_has_value_zero(self):
        self.assertEqual(0, self.uut.value)

    def test_numeric_character_retains_its_value(self):
        # We can override the existing value of the object
        self.uut.set('9')

        # Expected comes first, then the actual value
        self.assertEqual(9, self.uut.value)

    def test_appending_a_single_character_should_return_its_value(self):
        # We use append to add a character to the initially empty string
        self.uut.append("a")
        self.assertEqual(1, self.uut.value)

    def test_appending_multiple_characters_should_return_combined_value(self):
        self.uut.append("a")
        self.uut.append("b")
        self.uut.append("c")
        self.assertEqual(6, self.uut.value)

    def test_unsupported_characters_should_not_count(self):
        self.uut.set("=")
        self.assertEqual(0, self.uut.value)

        self.uut.set("#")
        self.assertEqual(0, self.uut.value)

        self.uut.set("-")
        self.assertEqual(0, self.uut.value)

    def test_what_more_can_you_think_of_to_test(self):
        # Can you come up with another test that you can run?
        ...

    def test_get_value_at_index_valid_index_valid_score(self):
        self.uut.set("HelloWorld")
        self.assertEqual(self.uut.get_value_at_index(1), 5)

        self.uut.set("ThisIsSoCool")
        self.assertEqual(self.uut.get_value_at_index(4), 9)


    def test_get_value_at_index_invalid_index_raises_index_error(self):
        self.uut.set("1")
        with self.assertRaises(IndexError):
            self.uut.get_value_at_index(1)
            self.uut.get_value_at_index(-1)


if __name__ == '__main__':
    unittest.main()
