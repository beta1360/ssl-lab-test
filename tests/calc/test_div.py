import unittest
from khleepkg03.app import Caculator

class TestPackage(unittest.TestCase):
    def test_module(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        dict = calc.getStatus()
        if self.assertFalse(dict["add"]): pass
        if self.assertFalse(dict["sub"]): pass
        if self.assertFalse(dict["mul"]): pass
        if self.assertTrue(dict["div"]): pass
        if self.assertTrue(dict["rem"]): pass

    def test_division_1(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        self.assertEqual(calc.division(4, 2), (2, 0))

    def test_division_2(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        self.assertEqual(calc.division(4, -2), (-2, 0))

    def test_division_3(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        self.assertEqual(calc.division(-4, -2), (2, 0))

    def test_division_4(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=False)
        self.assertEqual(calc.division(-4, 2), (-2, 0))

    def test_error_zero_division(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=False)
        try:
            calc.division(4, 0)
        except Exception as e:
            self.assertEqual(e, ZeroDivisionError)

    def test_type_1(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        with self.assertRaises(ValueError):
            calc.adder(0, 1)

    def test_type_2(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        with self.assertRaises(ValueError):
            calc.substraction(0, 1)

    def test_type_3(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        with self.assertRaises(ValueError):
            calc.multiplication(0, 1)

    def test_type_4(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=False)

        try:
            div, rem = calc.division(1, 2)
            print(div + " and " + rem)

        except Exception as e:
            if e != None: pass

if __name__ == "__main__":
    unittest.main()