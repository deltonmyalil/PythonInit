class Computer:
    def __init__(self,processor,RAM):
        self.processor = processor
        self.RAM = RAM

    def getSpecs(self):
        self.processor = input("Enter processor>>>")
        self.RAM = input("Enter RAM size>>>")

    def putSpecs(self):
        print("The chosen computer has {0} processor and {1} GB RAM".format(self.processor,self.RAM))


class LaptopComputer(Computer):
    def __init__(self,weight):
        self.weight = weight

    def putWeight(self):
        print("The chosen laptop weighs",self.weight,"kg")

    def getweight(self):
        self.weight = input("Enter weight of the laptop in kg")

class DesktopComputer(Computer):
    def __init__(self,caseColor):
        self.caseColor = caseColor

    def putCaseColor(self):
        print("The chosen Desktop case color is",self.caseColor)

    def getCaseColor(self):
        self.caseColor = input("Enter color of the cabinet")


type = input("Enter the type of computer - L for Laptop and D for Desktop>>>")
while(True):
    if type == "l" or type == "L":
        laptop = LaptopComputer("")
        laptop.getSpecs()
        laptop.getweight()
        laptop.putSpecs()
        laptop.putWeight()
    elif type =="d" or type == "D":
        desktop = DesktopComputer("")
        desktop.getSpecs()
        desktop.getCaseColor()
        desktop.putSpecs()
        desktop.putCaseColor()
    if input("Continue? Enter 'n' to terminate>>>") == "n":
        break