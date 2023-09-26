# encapsulation is data hiding
# we will be defining private and public members in code
# unlike other prog languages, python uses symbols instead of word reperesentation
# private = single underscore or double underscore

# first example
class price:

    # constructor
    def __init__(self):
        self.price1 = 400

    # method 1
    def sellPrice(self):
        sellPrice = self.price * (120/100)
        print("The selling price is : ",  sellPrice)

    # method 2
    '''def getprofit(self):
        profit = sellPrice - self.price1
        print("The profit is: ", profit)'''

    # create object
    markedP = price()


    # call the method
print(markedP.sellprice1())

# example two : derived class


class person:

    # constructor
    def __init__(self):
        self._name = " "
        self._salary = 0
        self._status = " "

    # create method
    def getName(self):
        name = input("Enter your name: ", )
        self._name = name
        print("Employee name: ", self._name)

    # method 2 : salary
    def getsalary(self):
        sal = int(input("Enter your salary: ",))
        self._salary = sal
        print("salary due: ", self._salary)

    # method 3

    def status(self):
        stat = input("Enter your employment status: ", )
        self._status = stat
        print("Employment status: ", self._status)

    # derived class
    class Newsalary(person):

        # method: calculate new salary
        def NewSalary(self):
            sal_new = self._salary * (115/100)
            print("New salary: ", )

    # create object
    Alice = person()
    Alice = Newsalary()

    # call on methid
    print(Alice.newSalary())
