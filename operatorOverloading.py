#create a class
class Point:

    def __init__(self,x,y):#define attribs in the class as usual - coordinates x and y
        self.x = x
        self.y = y

    def __add__(self, other):#this is built in func to perform opOverload on +
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

    def __str__(self): #to format the result as in string format
        return "{0},{1}".format(self.x,self.y)

point1 = Point(1,4)
point2 = Point(2,8)
print(point1+point2) #+ is overloaded with what is in __add__