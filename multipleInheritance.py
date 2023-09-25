#This will be a demo of multiple inheritance
#we will have parent classes and no super classes

#case 1: shopping centre
class supermarket:

    #constructor
    def __init__(self, grocery, detergents, bakery):
        self.grocery = grocery
        self.detergents = detergents
        self.bakery = bakery
    #method 1
    def getGrocery(self):
        groc = input("Enter your grocery of choice: ", )
        self.grocery = groc
        return self.grocery
    #method 2
    def getDetergent(self):
        deterg = input("Enter your detergent of choice: ", )
        self.grocery = deterg
        return self.detergents
    #method 3
    def getBakery(self):
        bake = input("Enter your confectionery of choice: ", )
        self.bakery = bake
        return self.bakery
    
#base class 2
class shop:

    #constructor
    def __init__(self, toiletries, crockery):
        self.toiletries = toiletries
        self.crockery = crockery
    #method
    def getStuff(self):
        toiletry = input("Enter your toiletry item: ", )
        self.toiletries = toiletry
        crock = input("Enter your crockery of choice: ", )
        self.crockery = crock
        return (self.toiletry + self.crockery)
    
#multiple inheritance
#derived class

class shopping(supermarket,shop):
    # due to the different constructors we initialize both constructors
    #we have created a new inherited constructor from both classes
    def __init__(self):
        supermarket.__init__(self, ' ', " ", " ")
        shop.__init__(self, " ", " ")
    #method
    def getList(self):
        print(self.bakery)
        print(self.grocery)
        print(self.detergents)
        print(self.toiletry)
        print(self.crockery)

    #create objects
    shopping = shopping()

    #calling
    print(shopping.getBakery())
    print(shopping.getDetergent())
    print(shopping.getStuff())
    print(shopping.getList())
    





#create objects

