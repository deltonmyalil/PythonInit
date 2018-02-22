class Overloading:
    def __init__(self,a):
        self.a = a

    def __mul__(self,other):
        return self.a+other.a

num1 = Overloading(4)
num2 = Overloading(5)
print(num1*num2)
