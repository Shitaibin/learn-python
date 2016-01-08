import unittest

from bar import dumb_true  # look here

class TestBar(unittest.TestCase):
    def test_bar_true(self):
        self.assertTrue(dumb_true())  


if __name__ == "__main__":
    unittest.main()