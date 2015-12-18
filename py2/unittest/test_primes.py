import unittest
from primes import *


class PrimesTestCase(unittest.TestCase):
    """
    Tests for primes.py.
    """

    def test_is_five_prime(self):
        """
        Is five successfuly determind to be prime?
        """
        self.assertTrue(is_prime(5), msg="5 is a prime")

    def test_is_four_not_prime(self):
        """
        Is four successfuly determind to be not prime?
        """
        self.assertFalse(is_prime(4), msg="4 is not a prime")

    # boundary test
    def test_is_0_not_prime(self):
        """
        Is 0 correctly determined not be prime?
        """
        self.assertFalse(is_prime(0), msg="0 is not a prime")

    def test_negative_number(self):
        """
        Is a negative number correctly determind not to be prime?
        """
        for num in range(-10, 0):
            self.assertFalse(is_prime(num),
                             msg="{} shoud determined not to be\
                              prime".format(num))


if __name__ == "__main__":
    unittest.main()
