from django.test import TestCase

# Create your tests here.
import unittest

class TestMyApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()