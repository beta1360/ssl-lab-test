import unittest
from khleepkg03.app import Caculator

class MyCalcTest(unittest.TestCase):
    def test_module(self):
        calc = Caculator(isAdd=False,
                 isSub=True,
                 isMul=False,
                 isDiv=False,
                 isRem=False)
        dict = calc.getStatus()
        if self.assertFalse(dict["add"]): pass
        if self.assertTrue(dict["sub"]): pass
        if self.assertFalse(dict["mul"]): pass
        if self.assertFalse(dict["div"]): pass
        if self.assertFalse(dict["rem"]): pass

    def test_substractor_1(self):
        calc = Caculator(isAdd=False,
                 isSub=True,
                 isMul=False,
                 isDiv=False,
                 isRem=False)
        sub = calc.substraction(1, 2)
        self.assertEqual(sub, -1,
                         msg="not equal:: %d != %d" %(sub, -1))

    def test_substractor_2(self):
        calc = Caculator(isAdd=False,
                 isSub=True,
                 isMul=False,
                 isDiv=False,
                 isRem=False)
        sub = calc.substraction(-1, 2)
        self.assertEqual(sub, -3,
                         msg="not equal:: %d != %d" %(sub, -3))

    def test_substractor_3(self):
        calc = Caculator(isAdd=False,
                 isSub=True,
                 isMul=False,
                 isDiv=False,
                 isRem=False)
        sub = calc.substraction(-1, -2)
        self.assertEqual(sub, 1,
                         msg="not equal:: %d != %d" %(sub, 1))

    def test_substractor_4(self):
        calc = Caculator(isAdd=False,
                 isSub=True,
                 isMul=False,
                 isDiv=False,
                 isRem=False)
        sub = calc.substraction(0, 0)
        self.assertEqual(sub, 0,
                         msg="not equal:: %d != %d" %(sub, 0))

    def test_type_1(self):
        calc = Caculator(isAdd=False,
                         isSub=True,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        with self.assertRaises(ValueError):
            calc.adder(0, 1)

    def test_type_2(self):
        calc = Caculator(isAdd=False,
                         isSub=True,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        with self.assertRaises(ValueError):
            calc.multiplication(0, 1)

    def test_type_3(self):
        calc = Caculator(isAdd=False,
                         isSub=True,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        with self.assertRaises(ValueError):
            calc.division(0, 1)

if __name__ == "__main__":
    unittest.main()