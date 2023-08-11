#bit operations
#using 3 methods, each using two concepts
#a function concept and inbuilt functions

#inbuilt function, DecimalToBinary() , bin()

def DecimalToBinary(n):
    return ("{0:b}".format(int(n)))

#calling a function
d = DecimalToBinary(9)
print(d)

#bin function
t = bin(14)
print(t)

#function call
d = DecimalToBinary(9)
print(d)

#function call two
r = bin(789)
print(r)


