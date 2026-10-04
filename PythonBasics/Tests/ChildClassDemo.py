from OOPsDemo import Calculator


class ChildImplementation (Calculator) :
    num2 = 200

    def __init__(self,):
        Calculator.__init__(self,10,5)

    def getCompleteData(self):
        return ChildImplementation.num2 + self.num + self.subtract()

childImplementation = ChildImplementation()
print(childImplementation.getCompleteData())


