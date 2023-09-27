

class animal:
    def __init__(self):
        self.movement = " "
        self.sound = " "
        self.name = " "

# form 1: cat


class cat(animal):
    def getName(self):
        name = input("Please enter the cat name: ",)
        self.name = name
        return self.name

# form two: dog


class dog(animal):
    def getName_1(self):
        name_1 = input("enter the dogs name: ", )
        self.name = name_1
        return self.name

# form 3: parrot


class parrot(animal):
    def getName_2(self):
        name_2 = input("enter the parrots name: ", )
        self.name = name_2
        return self.name


# objects
cat = cat()
dog = dog()
parrot = parrot()

# call method
print(cat.getName())
print(dog.getName_1())
print(parrot.getName_2())
