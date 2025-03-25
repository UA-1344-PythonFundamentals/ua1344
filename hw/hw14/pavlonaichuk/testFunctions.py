import unittest
import copy
import functions
import functions_with_errors


class CompareModulesTest(unittest.TestCase):

    def test_greeting_by_name(self):
        name = "Alice"
        expected = "Hello Alice!"
        self.assertEqual(functions.greeting_by_name(name), expected, "functions.greeting_by_name is incorrect")
        self.assertEqual(functions_with_errors.greeting_by_name(name), expected, "functions_with_errors.greeting_by_name is incorrect")

    def test_get_symbol_position_success(self):
        text, symbol = "hello", "e"
        expected = 2
        self.assertEqual(functions.get_symbol_position(text, symbol), expected, "functions.get_symbol_position is incorrect")
        self.assertEqual(functions_with_errors.get_symbol_position(text, symbol), expected, "functions_with_errors.get_symbol_position is incorrect")

    def test_get_symbol_position_not_found(self):
        text, symbol = "hello", "z"
        expected = "Not found"
        self.assertEqual(functions.get_symbol_position(text, symbol), expected)
        self.assertEqual(functions_with_errors.get_symbol_position(text, symbol), expected)

    def test_get_symbol_position_invalid_symbol(self):
        text, symbol = "el"
        expected = "Error! Symbol can be string with only one letter"
        self.assertEqual(functions.get_symbol_position("hello", symbol), expected)
        self.assertEqual(functions_with_errors.get_symbol_position("hello", symbol), expected)

    def test_merge_result(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        expected = {"a": 1, "b": 2}
        self.assertEqual(functions.merge(d1, d2), expected)
        self.assertEqual(functions_with_errors.merge(d1.copy(), d2), expected)

    def test_merge_dict1_immutability(self):
        d1 = {"x": 10}
        d2 = {"y": 20}
        original = copy.deepcopy(d1)

        _ = functions.merge(d1, d2)
        self.assertEqual(d1, original, "functions.merge modifies dict1")

        d1 = {"x": 10}
        original = copy.deepcopy(d1)
        _ = functions_with_errors.merge(d1, d2)
        self.assertEqual(d1, original, "functions_with_errors.merge modifies dict1")


if __name__ == "__main__":
    unittest.main()
