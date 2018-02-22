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
        print("The Name is",self.name," and the contact number is ",self.contact)

#Once the attribs and the methods are defined, we need to create the objects
John = Students("Null",0) #This means that john is one of the objects of the Students class.
#                           Also, Students have two attribs ie one string and one number
#                           Hence, we have to initialize with the attribs of the class while creating an object of the class to avoid error
John.getData()
John.putData()