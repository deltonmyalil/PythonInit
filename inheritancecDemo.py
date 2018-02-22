class Students:
    def __init__(self,name,contact): #to define attribs of the class use def __init__(self,<attribute1>,<attribute2>,...)
        self.name = name
        self.contact = contact #name and contact are attribs and they are to be defined like this

    #once attribs are defined, you have to define the methods of the class

    def getData(self): #This is a method
        print("Accepting data")
        self.name = input("Enter Name>>>")
        self.contact = input("Enter Contact>>>")

    def putData(self):
        print("The Name is",self.name," and the contact number is ",self.contact,"His age is",self.age)

class ScienceStudents(Students):#ScienceStudents inherited the methods from Students
    def __init__(self,age):
        self.age = age

    def science(self):
        print("Im a science student")

Rob = ScienceStudents(20)
Rob.science()
Rob.getData()
Rob.putData()