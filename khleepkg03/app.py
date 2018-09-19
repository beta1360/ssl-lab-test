
class Caculator:
    def __init__(self, isAdd, isSub, isMul, isDiv, isRem):
        self.isAdd = isAdd
        self.isSub = isSub
        self.isMul = isMul
        self.isDiv = isDiv
        self.isRem = isRem

    def adder(self, num1, num2):
        if self.isAdd:
            sum = num1 + num2
            return sum
        else:
            raise(ValueError)

    def substraction(self, num1, num2):
        if self.isSub:
            return (num1 - num2)
        else:
            raise(ValueError)

    def multiplication(self, num1, num2):
        if self.isMul:
            return (num1 * num2)
        else:
            raise(ValueError)

    def division(self, num1, num2):
        if self.isDiv:
            try:
                n = num1 / num2
                r = num1 % num2

                if self.isRem:
                    return n, r
                else:
                    return n

            except ZeroDivisionError as e:
                raise (e)

        else:
            raise(ValueError)

    def getStatus(self):
        return {
            "add": self.isAdd,
            "sub": self.isSub,
            "mul": self.isMul,
            "div": self.isDiv,
            "rem": self.isRem
        }

