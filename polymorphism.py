# the existense of an object in many forms

# case study one

class circle:
    # constructor
    def __init__(self):
        self.pi = 3.142
        self.radius = 0

    # method
    def Radius(self):
        radius = int(input("please enter the radius value: ", ))
        self.radius = radius
        print("The radius is: ", self.radius)

    # form 1 cylinder pir2h


class cylinder(circle):

    # method 1
    def render(self):
        height = int(input("enter the height: ", ))
        vol = self.pi * self.radius * self.radius * height
        print("The volume is: ,vol")

    # form  sphere


class sphere(circle):

    # method 1
    def render(self):
        surface = 4/3 * self.radius * self.radius * self.radius * self.pi
        print("The surface area is: ", surface)

    # create object
sphere1 = sphere()
cylinder1 = cylinder()

# methods
print(sphere1.radius())
print(sphere.SA())
