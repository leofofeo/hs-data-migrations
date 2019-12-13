import unittest
from credentials import APIKeys

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.api_keys = APIKeys('abc', 'def')

    def test_from_key(self):
        self.assertEqual(self.api_keys.get_from_key(), 'abc')
    
    def test_to_key(self):
        self.assertEqual(self.api_keys.get_to_key(), 'def')


if __name__ == '__main__':
    unittest.main()