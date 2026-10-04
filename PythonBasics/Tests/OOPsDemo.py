class Calculator:
    num = 100

    def __init__(self,number1,number2):
        self.firstNumber = number1
        self.secondNumber = number2
        print("I am called automatically when object is created")


    def getData(self):
        print("I am not executing method in class Calculator")
        #self.num = self.num + 1
        #return self.num

    def  subtract(self):
        return self.firstNumber - self.secondNumber + Calculator.num

obj = Calculator(10,3)
obj.getData()
print(obj.num)
print(obj.subtract())

print("------------------------------------")
obj2 = Calculator(5,4)
obj2.getData()
print(obj2.num)
print(obj2.subtract())

# def add(number1,number2):
#     return number1 + number2
