import unittest
from khleepkg03.app import Caculator

calc = Caculator(True, True, True, True, True)
dict = calc.getStatus()

class MyCalcTest(unittest.TestCase):
    def test_module_adder(self):
        # Member Value: Dict["add"]
        if self.assertTrue(dict["add"]):
            pass

    def test_module_substract(self):
        # Member Value: Dict["sub"]
        if self.assertTrue(dict["sub"]):
            pass

    def test_module_multiplication(self):
        # Member Value: Dict["mul"]
        if self.assertTrue(dict["mul"]):
            pass

    def test_module_division(self):
        # Member Value: Dict["div"]
        if self.assertTrue(dict["div"]):
            pass

    def test_module_reminder(self):
        # Member Value: Dict["rem"]
        if self.assertTrue(dict["rem"]):
            pass

if __name__ == "__main__":
    unittest.main()