import unittest
from primes import is_prime, get_next_prime


class PrimesTestCase(unittest.TestCase):
    """
    Unit test for primes.py
    """

    def setUP(self):
        """
        Here to create object.
        And this object be used in any function.
        """
        pass

    def tearDown(self):
        """
        Clean objects created in setUP.
        """
        pass

    def test_is_prime(self):
        """
        test function is_prime.
        """
        prime_num = [2, 3, 5, 7, 11]
        for num in prime_num:
            self.assertTrue(is_prime(num),
                            msg="{} should determined be prime".format(num))

        # test none primes wihch bigger than 2
        not_prime_num = [4, 6, 8, 10, 12]
        for num in not_prime_num:
            self.assertFalse(is_prime(num),
                             msg="{} should not determined\
                             be prime".format(num))

        # test none primes wich smaller than 2
        for num in range(-10, 2):
            self.assertFalse(is_prime(num),
                             msg="{} should not determined\
                             be prime".format(num))


    def test_get_next_prime(self):
        """
        Test function get_next_prime.
        """
        # m < 2 and m is not a prime
        self.assertEqual(get_next_prime(-1), 2,
                         msg="2 should be the next prime of -1")
        # m >= 2 and m is a prime
        self.assertEqual(get_next_prime(2), 3,
                         msg="3 should be next prime of 2")
        self.assertEqual(get_next_prime(3), 5,
                         msg="5 should be next prime of 3")
        self.assertEqual(get_next_prime(23), 29,
                         msg="29 should be next prime of 23")
        # m >= 2 and m is not a prime
        self.assertEqual(get_next_prime(4), 5,
                         msg="5 should be next prime of 4")
        self.assertEqual(get_next_prime(20), 23,
                         msg="23 should be next prime of 20")
        ##################################
        #
        self.assertNotEqual(get_next_prime(3), 4,
                         msg="4 should not determinded be the next prime of 20")


#####################################################
# Test suite
def suite():
    """
    Make suite, make these functions, which you
    want to test in to one.

    You can also use function makeSuite to
    get an suite.
    """
    suite = unittest.TestSuite()
    suite.addTest(PrimesTestCase("test_is_prime"))
    return suite


###################################################
# Using makeSuite to get an suite
#suite = unittest.makeSuite(PrimesTestCase, 'test')

if __name__ == '__main__':
    unittest.main()

    # run suite
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
