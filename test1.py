import unittest
import program

class fractionTestCase(unittest.TestCase):
    def testFraction(self):
        self.assertEqual(program.checkFraction(1/3,1/5),True)

if __name__ == '__main__':
    unittest.main()