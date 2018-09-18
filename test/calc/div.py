import unittest
from main.calc import Caculator

class MyCalcTest(unittest.TestCase):
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
        div, rem = calc.division(4, 2)
        self.assertEqual(div, 2,
                         msg="not equal:: %d != %d" %(div, 2))
        self.assertEqual(rem, 0,
                         msg="not equal:: %d != %d" %(div, 0))

    def test_division_2(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        div, rem = calc.division(-4, 2)
        self.assertEqual(div, -2,
                         msg="not equal:: %d != %d" %(div, -2))
        self.assertEqual(rem, 0,
                         msg="not equal:: %d != %d" %(div, 0))

    def test_division_3(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        div, rem = calc.division(-4, -2)
        self.assertEqual(div, 2,
                         msg="not equal:: %d != %d" %(div, 2))
        self.assertEqual(rem, 0,
                         msg="not equal:: %d != %d" %(div, 0))

    def test_division_4(self):
        calc = Caculator(isAdd=False,
                         isSub=False,
                         isMul=False,
                         isDiv=True,
                         isRem=True)
        div = calc.division(4, 0)
        self.assertRaises(ZeroDivisionError)

if __name__ == "__main__":
    unittest.main()