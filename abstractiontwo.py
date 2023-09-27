# second abstraction example
# the case study will be for company protocol

class complaint:
    def __init__(self):
        self.name = " "
        self.sku_no = 0
        self.complaint = " "

    # method 1
    def compain(self):
        pass

    # method two
    def info(self):
        pass

    # method 3:
    def submit(self):
        pass

# client 1


class client_1(complaint):
    def __init__(self):
        self.name = " "
        self.complaint = " "
        self.sku_no = 0

    # method 1
    def comp1(self):
        complaint = input("Enter the clients concern: ", )
        self.complaint = complaint
        print("The clients issue is: ", self.complaint)

    # method 2
    def info(self):
        Nclient = input("Enter the clients name: ", )
        sku_no = int(input("enter the Sku No: ", ))
        self.sku_no = sku_no
        self.name = Nclient
        print("client name: ", self.name)
        print("sku Number: ", self.sku_no)

    # method 3
    def status(self):
        status = input("Is the issue resolved: ", ).lower()
        # decision tree
        if (status == 'yes'):
            print("The complaint has been resolved")
        else:
            print("The complaint needs attention")


# objects
mark = client_1()

# call method
print(mark.comp1())
print(mark.info())
print(mark.status())
