import unittest
from functions import greeting_by_name, get_symbol_position, merge
from functions_with_errors import greeting_by_name, get_symbol_position, merge

class TestMyFunction(unittest.TestCase):
    
    # greeting_by_name
    def test_greeting_by_name_correct(self):
        self.assertEqual(greeting_by_name("Alice"), "Hello Alice!")  
    
    def test_greeting_wrong_name(self):
        self.assertNotEqual(greeting_by_name("Charlie"), "Hello Addison")
        
    def test_greeting_by_name_error(self):
        self.assertEqual(greeting_by_name("Alice"), "Hello name!")  
        
    # get_symbol_position
    def test_symbol_position(self):
        self.assertEqual(get_symbol_position("Hello, world!", "o"), 5)  
    
    def test_symbol_wrong_position(self):
        self.assertNotEqual(get_symbol_position("Hello, world!", "o"), 4)  
        
    def test_more_symbols(self):
        self.assertEqual(get_symbol_position("Hello, world!", "lo"), "Error! Symbol can be string with only one letter")  
                
    def test_wrong_index(self):
        self.assertNotEqual(get_symbol_position("Hello, world!", "H"), 0)  
        
    def test_symbol_not_found(self):
        self.assertEqual(get_symbol_position("Hello, world", "a"), "Not found")  
        
    def test_upper_lower_case(self):
        self.assertEqual(get_symbol_position("Hello, world", "h"), "Not found")  
        
    def test_empty_string(self):
        self.assertEqual(get_symbol_position("", "o"), "Not found")  
    
    def test_empty_symbol(self):
        self.assertEqual(get_symbol_position("Hello, world", " "), 7)
        
    # merge
    def test_merge(self):
        self.assertEqual(merge({"a": 1, "b": 2, "c": 3}, {"b": 3, "c": 4, "d": 5}), {"a": 1, "b": 3, "c": 4, "d": 5})  
        
    def test_wrong_merge(self):
        self.assertNotEqual(merge({"a": 1, "b": 2, "c": 3}, {"b": 3, "c": 4, "d": 5}), {"a": 1, "b": 2, "c": 3, "d": 5}) 
    
    def test_empty_dict1(self):
        self.assertEqual(merge({"a": 1, "b": 2, "c": 3}, {}), {"a": 1, "b": 2, "c": 3})  
    
    def test_empty_dict2(self):
        self.assertEqual(merge({}, {"a": 1, "b": 2, "c": 3}), {"a": 1, "b": 2, "c": 3})  
    
    def test_two_empty_dicts(self):
        self.assertEqual(merge({}, {}), {})  

if __name__ == '__main__':
    unittest.main()
