import unittest

from main import isbn10_checker, isbn13_checker


class MyTestCase(unittest.TestCase):
    def test_isbn10(self):
        test = isbn10_checker("0-7167-0344-0")
        self.assertEqual(True, test)  # add assertion here

    def test_isbn13(self):
        test = isbn13_checker("9780716703440")
        self.assertEqual(True, test)
if __name__ == '__main__':
    unittest.main()
