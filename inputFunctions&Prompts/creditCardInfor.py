print("Kindly help us fill the  following information")
print("What is your credit card number: ")
Number = input()

if Number.isdigit():
           print(Number, "is an integer.")
else:
        print(Number, "is a string.")
        