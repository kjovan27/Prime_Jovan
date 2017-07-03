import unittest
from prime import is_prime

class PrimeTestCase(unittest.TestCase):

    def test_is_zero_prime(self):
        self.assertTrue(is_prime(0))

if __name__ == '__main__':
    unittest.main()
