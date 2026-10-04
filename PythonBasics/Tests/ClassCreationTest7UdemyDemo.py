class BasicCalculator:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        return self.number1 + self.number2

    def subtraction(self):
        return self.number1 - self.number2

    def multiplication(self):
        return self.number1 * self.number2

    def division(self):
        return self.number1 / self.number2


basic_calculator = BasicCalculator(10,5)
print("Addition: 10 + 5 = ",basic_calculator.addition())
print("Subtraction: 10 - 5 = ",basic_calculator.subtraction())
print("Multiplication: 10 * 5 = ",basic_calculator.multiplication())
print("Division: 10 / 5 = ",basic_calculator.division())

#Test 7 Passed