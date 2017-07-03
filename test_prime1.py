import unittest
from prime import is_prime

class PrimeTestCase(unittest.TestCase):

    def test_is_zero_prime(self):
        self.assertFalse(is_prime(0))
        
    def test_is_four_prime(self):
        self.assertFalse(is_prime(4))
        
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))
        
    def test_negative_number(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))
        
    def test_isNot_string(self):
        self.assertFalse(is_prime(type == string))

if __name__ == '__main__':
    unittest.main()
