import calculator
import unittest

class test_Assert(unittest.TestCase):
    def test_divi(self):
        self.assertEqual(calculator.divi(6,2),4)

if __name__=="__main__":
    unittest.main()