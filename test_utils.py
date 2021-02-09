# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5),120)
        self.assertEqual(utils.fact(0),1)
        self.assertEqual(utils.fact(-1),ValueError)
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,2,1))
    
    def test_integrate(self):
        self.assertEqual(utils.integrate('x**3',0,2),4.0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
