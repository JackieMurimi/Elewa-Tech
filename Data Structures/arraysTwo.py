# they hold only one data type in a single array of data items

# syntax
# import the array module
# arrayName = stated_array.array the module("data_type", [data items])

# demo 1
import array as Type

# create the array
myArray = Type.array("i", [23, 14, 17, 34])
myArray2 = Type.array("i")

# methods
# append()
'''var_1 = 23
var_2 = 45
var_3 = int(input("Enter a number: "))
var_4 = int(input("Enter a number: "))

myArray2.append(var_1)
myArray2.append(var_2)
myArray2.append(var_3)
myArray2.append(var_4)'''

# insert()
# we use u for characters
myArray3 = Type.array("u")

# variables
var_a = "x"
var_b = "y"
var_c = "z"
var_d = input("Enter a character value: ")
var_e = input("Enter a character value: ")

myArray3.insert(3, var_a)
myArray3.insert(1, var_b)
myArray3.insert(0, var_c)
myArray3.insert(2, var_d)
myArray3.insert(4, var_e)

print(myArray3)
print(myArray3[3])


# we use f for float
myArray4 = Type.array("f")
myArray4.insert(0, 3.14)
print(myArray4)


print(myArray)
print(myArray[0:2])
print(myArray[:2])
print(myArray2)
