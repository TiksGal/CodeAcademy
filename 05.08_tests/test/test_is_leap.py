import unittest
from main import is_leap

class TestIsLeap(unittest.TestCase):
    def test_return_true_when_year_is_leap(self):
        result = is_leap(2000)
        self.assertTrue(result)
    
    def test_return_false_when_year_not_leap(self):
        result = is_leap(2100)
        self.assertFalse(result)
    
    def test_raises_error_when_str_is_pass(self):
        with self.assertRaises(TypeError):
            is_leap("2000")