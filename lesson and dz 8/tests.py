import  unittest
from lesson_8_2 import *

class MyTest(unittest.TestCase):

    def test_args(self):
        self.assertEqual(adder(2, 2),5)

    def test_zero_args(self):
        self.assertEqual(adder(0, 0),1)

    def test_zero1_args(self):
        self.assertEqual(adder(-3, -5),-8)

if __name__ == '__main__':
    unittest.main()