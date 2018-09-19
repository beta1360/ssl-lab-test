import unittest
from khleepkg03.app import Caculator

class MyCalcTest(unittest.TestCase):
    def test_module(self):
        calc = Caculator(isAdd=True,
                         isSub=False,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        dict = calc.getStatus()
        if self.assertTrue(dict["add"]): pass
        if self.assertFalse(dict["sub"]): pass
        if self.assertFalse(dict["mul"]): pass
        if self.assertFalse(dict["div"]): pass
        if self.assertFalse(dict["rem"]): pass

    def test_adder_1(self):
        calc = Caculator(isAdd=True,
                         isSub=False,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        sum = calc.adder(1, 2)
        self.assertEqual(sum, 3,
                         msg="not equal:: %d != %d" %(sum, 3))

    def test_adder_2(self):
        calc = Caculator(isAdd=True,
                         isSub=False,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        sum = calc.adder(-1, 2)
        self.assertEqual(sum, 1,
                         msg="not equal:: %d != %d" %(sum, 1))

    def test_adder_3(self):
        calc = Caculator(isAdd=True,
                         isSub=False,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        sum = calc.adder(-1, -2)
        self.assertEqual(sum, -3,
                         msg="not equal:: %d != %d" %(sum, -3))

    def test_adder_4(self):
        calc = Caculator(isAdd=True,
                         isSub=False,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        sum = calc.adder(0, 0)
        self.assertEqual(sum, 0,
                         msg="not equal:: %d != %d" %(sum, 0))

    def test_type_1(self):
        calc = Caculator(isAdd=True,
                         isSub=False,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        with self.assertRaises(ValueError):
            calc.substraction(0, 1)

    def test_type_2(self):
        calc = Caculator(isAdd=True,
                         isSub=False,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        with self.assertRaises(ValueError):
            calc.multiplication(0, 1)

    def test_type_3(self):
        calc = Caculator(isAdd=True,
                         isSub=False,
                         isMul=False,
                         isDiv=False,
                         isRem=False)
        with self.assertRaises(ValueError):
            calc.division(0, 1)

if __name__ == "__main__":
    unittest.main()