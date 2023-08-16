#Write codes to convert the following into Bits
#12
def DecimalToBinary(n):
    return ("{0:b}".format(int(n)))
a = DecimalToBinary(12)
print(a)

b = DecimalToBinary(34)
print(b)

c = DecimalToBinary(65)
print(c)

d= DecimalToBinary(456)
print(d)

#Write a Python program that will allow you to convert numbers into Bits
e = 93

# Base 2(binary)
binary_e = bin(e)
print(binary_e)
print(int(binary_e, 2))
#Write a python program using user defined Functions that will allow you to convert the following into Bits and To decimals
#110111
#010111100
#1001000110

def BinToDec(b):
    return int(b, 2)

#print("Enter the Binary Number: ", end="")
#binaryNumber = input()

#decimalNumber = BinToDec(binaryNumber)
#print("\nEquivalent Decimal Value = ", decimalNumber)

binaryNumber_f = 110111
decimalNumber_f = BinToDec(binaryNumber_f)
print(binaryNumber_f)
