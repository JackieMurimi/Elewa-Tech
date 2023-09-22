#we are cdreating a class that holds properties only
#inherit the properties to create methods
#ccreate ojects from the class
#__init__ __

class fruits:
    def __init__ (self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
#inherited class to hold methods
class info(fruits):
    def getName(self):
        return self.name
    #method 1: color
    def getColor(self):
        color = input("the color is: ", )
        self.color = color
        return self.color
    def totalPrice(self):
        cost = int(input("Enter the price of 1: ", ))
        num = int(input("Enter the total number you are buying: ", ))
        total = cost * num
        self.price = total
        return self.price

#create an object
banana = info("Banana", " ", 0)
print(banana.totalPrice())
print(banana.getColor())

