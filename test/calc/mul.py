import unittest
from khleepkg03.app import Caculator

calc = Caculator(isAdd=False,
                 isSub=False,
                 isMul=True,
                 isDiv=False,
                 isRem=False)

class MyCalcTest(unittest.TestCase):
    def test_module(self):
        dict = calc.getStatus()
        if self.assertFalse(dict["add"]): pass
        if self.assertFalse(dict["sub"]): pass
        if self.assertTrue(dict["mul"]): pass
        if self.assertFalse(dict["div"]): pass
        if self.assertFalse(dict["rem"]): pass

    def test_multiplication_1(self):
        mul = calc.multiplication(4, 2)
        self.assertEqual(mul, 8,
                         msg="not equal:: %d != %d" %(mul, 8))

    def test_multiplication_2(self):
        mul = calc.multiplication(-4, 2)
        self.assertEqual(mul, -8,
                         msg="not equal:: %d != %d" %(mul, -8))
    def test_multiplication_3(self):
        mul = calc.multiplication(-4, -2)
        self.assertEqual(mul, 8,
                         msg="not equal:: %d != %d" %(mul, 8))

    def test_multiplication_4(self):
        mul = calc.multiplication(4, 0)
        self.assertEqual(mul, 0,
                         msg="not equal:: %d != %d" %(mul, 0))

    def test_multiplication_5(self):
        mul = calc.multiplication(4, 0.5)
        self.assertEqual(mul, 2,
                         msg="not equal:: %d != %d" %(mul, 2))

if __name__ == "__main__":
    unittest.main()