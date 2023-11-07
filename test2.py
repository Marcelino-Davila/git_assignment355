import unittest
import program 

class fractionTestCase(unittest.TestCase):
    def testFraction(self):
        self.assertEqual(program.checkFraction(1/10,1/5),False)
if __name__ == '__main__':
    unittest.main()