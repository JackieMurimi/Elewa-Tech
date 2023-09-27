# we will be drawing an abstract class for shapes
# then we will use that information to build real classes

# shape example
# abstract class
class shape:
    def __init__(self):
        self.name = " "

    # method 1: perimeter
    def area(self):
        # Statements
        pass

    # method two: area
    def area(self):
        # statements
        pass
    # method 3: print statement

    def fact(self):
        # statements
        pass

# Real classes


class circle(shape):

    # constructor
    def __init__(self):
        self.name = " "
        self.radius = 0

    # method 1
    def cperimeter(self):
        radius = int(input("Enter the radius: ",))
        self.radius = radius
        perimeter = 3.142 * (self.radius * 2)
        print(perimeter)

    # method 2
    def cArea(self):
        radius = int(input("Enter the radius: ",))
        self.radius = radius
        area = 3.14 * self.radius * self.radius
        print(area)

    # method 3
    def fact(self):
        name = input("Enter the shape name: ", )
        self.name = name
        print("The shape is a ", self.name)


# shape two:
class Rectangle(shape):
    def __init__(self):
        self.name = " "
        self.length = 0
        self.width = 0

    # method 1
    def Rperimeter(self):
        len = int(input("enter the length: ", ))
        wid = int(input("enter the width: ", ))
        self.length = len
        self.width = wid
        perimeter_r = 2 * (self.length + self.width)
        print(perimeter_r)

    # method two
    def Rarea(self):
        len = int(input("enter the length: ", ))
        wid = int(input("enter the width: ", ))
        self.length = len
        self.width = wid
        area_r = self.length * self.width
        print(area_r)

    # method 3
    def Rfact(self):
        name_r = input("Enter the name of the shape: ", )
        self.name = name_r
        print("The name of the shape is ", self.name)

    # create objects
rect = Rectangle()
circ = circle()

# call methods
print(circ.fact())
print(rect.Rarea())
