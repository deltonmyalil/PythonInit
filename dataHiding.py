class MyClass:
    __hiddenvar = 2  # __ ie dunders before a variable name will make it hidden. ie it will not be accessed outside this class
    publicvar = 3  # no dunders before varName ie it is not hidden

    def addHidden(self, incr):
        self.__hiddenvar += incr  # This car is unavailable outside the class
        print(self.__hiddenvar)

    def addPublic(self, incr):
        self.publicvar += incr  # This is a normal publiic variable
        print(self.publicvar)


obj = MyClass()
obj.addHidden(5)
obj.addPublic(5)
print(obj.publicvar)  # to access a var inside an obj of a class, use dot operator on obj followed by varName
print(
    obj.__hiddenvar)  # This gives error - "MyClass object has no attribute '__hiddenvar'" because the __hiddenvar is hidden
