import unittest

from foo import bar

class TestBar(unittest.TestCase):
    def test_bar_true(self):
        self.assertTrue(bar.dumb_true())


if __name__ == "__main__":
    unittest.main()