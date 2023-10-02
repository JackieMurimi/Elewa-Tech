#this is a sequential data structure
#its mutable(changeable)

#lists data structure demos
#creating lists
Fruits = []

#inserting operations
#hard code var
FA = "Banana"
FB = "Apple"
FC = "Mango"
FD = "Orange"

#prompt the user
#input( the variable)
'''FE = input("Enter the frut name: ", )
Fruits.append(FE)
FG = int(input("Enter a random number: ", ))
Fruits.append(FG)'''


#append() to add the data items
Fruits.append(FA)
Fruits.append(FB)
Fruits.append(FC)
Fruits.append(FD)

#data type
print(Fruits)


#insert() function
var = " Pineapple"
var_1 = 65
var_3 = True

#adding data item using the insert function
Fruits.insert(4, var)
Fruits.insert(0, var_1)
Fruits.insert(2, var_3)

'''print(Fruits)
print(Fruits[3])
print(Fruits[2])'''


#concatenation
#Its the process of combining two lists to make one whole new list
fruit = ["Oranges", "Avocado", "Grapes"]

#concat symbol is a +
NewFruits = Fruits + fruit
print(NewFruits)



