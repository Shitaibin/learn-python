import unittest


class AssertEqualTestCase(unittest.TestCase):
    """

    """

    def test_dict(self):
        """

        :return:
        """
        # the content of dict is the same, but with different order
        dict1 = {0: "a", 1: "b"}
        dict2 = {1: "b", 0: "a"}

        self.assertEqual(dict1, dict2)


if __name__ == "__main__":
    unittest.main()
