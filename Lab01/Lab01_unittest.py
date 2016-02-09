# unittest learning document

import unittest

from Lab01/Lab01 import Competitor


class Test_Lab01(unittest.TestCase):

    def competitor_test_equality(self):
        c1 = Competitor("Bob", "bob@gmail.com")
        c2 = Competitor("Tim", "tim@gmail.com", "Toronto")
        c3 = Competitor("Tim", "tim@gmail.com", "Toronto, Canada")
        self.assertEqual(c1 == c2, False)
        self.assertEqual(c2 == c3, True)
