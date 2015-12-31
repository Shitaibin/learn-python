import unittest
from unittest import TestCase
from assert_raises import type_error


class assert_raises_TestCase(TestCase):
    """
    unittest for assert_raises.py
    """

    def test_type_error(self):
        """
        """
        self.assertRaises(TypeError, lambda: type_error())
