import unittest

from main import isbn10_checker


class MyTestCase(unittest.TestCase):
    def test_isbn(self):
        test = isbn10_checker("0716703440")
        self.assertEqual(0, test)  # add assertion here


if __name__ == '__main__':
    unittest.main()
