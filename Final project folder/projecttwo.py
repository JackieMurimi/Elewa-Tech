# Hierarchy with Inheritance and Polymorphism using vehicles

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        pass

    def display_info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def drive(self):
        return "The car is roadworthy."

class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def drive(self):
        return "The truck is roadworthy."

    def display_info(self):
        return f"{super().display_info()} with a capacity of {self.capacity} tons"

class Motorcycle(Vehicle):
    def drive(self):
        return "The motorcycle is roadworthy."

def main():
    car = Car("Toyota", "Crown")
    truck = Truck("Ford", "F150", 5)
    motorcycle = Motorcycle("Boxer", "E50")

    vehicles = [car, truck, motorcycle]

    for vehicle in vehicles:
        print(vehicle.display_info())
        print(vehicle.drive())
        print("")

if __name__ == "__main__":
    main()
