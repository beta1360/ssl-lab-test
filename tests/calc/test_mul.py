import unittest
from khleepkg03.app import Caculator

class TestPackage(unittest.TestCase):
    def test_module(self):
        calc = Caculator(isAdd=False,
                 isSub=False,
                 isMul=True,
                 isDiv=False,
                 isRem=False)
        dict = calc.getStatus()
        if self.assertFalse(dict["add"]): pass
        if self.assertFalse(dict["sub"]): pass
        if self.assertTrue(dict["mul"]): pass
        if self.assertFalse(dict["div"]): pass
        if self.assertFalse(dict["rem"]): pass

    def test_multiplication_1(self):
        calc = Caculator(isAdd=False,
                 isSub=False,
                 isMul=True,
                 isDiv=False,
                 isRem=False)
        self.assertEqual(calc.multiplication(4, 2), 8)

    def test_multiplication_2(self):
        calc = Caculator(isAdd=False,
                 isSub=False,
                 isMul=True,
                 isDiv=False,
                 isRem=False)
        self.assertEqual(calc.multiplication(-4, 2), -8)

    def test_multiplication_3(self):
        calc = Caculator(isAdd=False,
                 isSub=False,
                 isMul=True,
                 isDiv=False,
                 isRem=False)
        self.assertEqual(calc.multiplication(-4, -2), 8)

    def test_multiplication_4(self):
        calc = Caculator(isAdd=False,
                 isSub=False,
                 isMul=True,
                 isDiv=False,
                 isRem=False)
        self.assertEqual(calc.multiplication(-4, 0), 0)

    def test_multiplication_5(self):
        calc = Caculator(isAdd=False,
                 isSub=False,
                 isMul=True,
                 isDiv=False,
                 isRem=False)
        self.assertEqual(calc.multiplication(4, 0.5), 2)

    def test_type_1(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=True,
                         isDiv=False,
                         isRem=False)
        with self.assertRaises(ValueError):
            calc.adder(0, 1)

    def test_type_2(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=True,
                         isDiv=False,
                         isRem=False)
        with self.assertRaises(ValueError):
            calc.substraction(0, 1)

    def test_type_3(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=True,
                         isDiv=False,
                         isRem=False)
        with self.assertRaises(ValueError):
            calc.division(0, 1)

if __name__ == "__main__":
    unittest.main()