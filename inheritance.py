#understanding class inheritance
#The syntax is as sollows

'''class base_class:
    properties

class derived_class(base_class):
    methods'''

class person:
    def _init_ (self, name, age):
        self.name = name
        self.age = age

        #method 1
    def getName(self):
        return self.name
        #method two
    def getAge(self):
        return self.age
        
    #derived class 1: education
class Education(person):
        #method: educated
    def isEducated(self):
        return True
#objects created
person_1 = person("Hailey", 23)
person_1 = Education("Hailey", 23)

#print statements
print(person_1.isEducated())
print(person_1.getAge())

#example 2
class Electric_shop:
     
     #constructor
    
 def _init_ (self, pd_name, quantity, price):
          self.name = pd_name
          self.quantity = quantity
          self.price = price

class methods(Electric_shop):
 def getName(self):
     return self.name
 def getQuantity(self):
          Quantity = int(input("please input the quantity: ", ))
          self.quantity = Quantity
          return self.quantity
     
 def getPrice(self):
          cost = int(input("Enter the cost: ", ))
          self.price = self.quantity * cost
          return self.price

#object methods
laptop = methods("Hellewett Pack", 0, 0)
print(laptop.getQuantity())

#price
print(laptop.getPrice())
     

#example 3
class Electric_shop:
    def _init_ (self, pd_name, quantity, price):
         self.name = pd_name
         self.quantity = quantity
         self.price = price

class name(Electric_shop):
    #create a new constructor
    def _init_ (self, pd_name, quantity, price):
         self.sname = pd_name
         self.squantity = quantity
         self.sprice = price
     
    def getname(self):
        name = input("Enter the device name: ", )
        self.name = name
        return self.name
    
#inherit from name
class laptop(name):
    def getPrice(self):
         price = int(input("Enter the price: ", ))
         self.sprice = price
         return self.sprice
    
#creating an object
lappy = laptop("Asus", 0, 0)
print(lappy.getPrice)


     