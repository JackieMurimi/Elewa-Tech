# a stack is build using two methods
# one using lists and the second one arrays
# to access data inside a stack, one must  use a method called pop()

# simple demo
myStack = []

# we will add data using the append function(This is how we push data inside a stack)
myStack.append("I")
myStack.append("love")
myStack.append("travelling")

print(myStack)

# how to access data inside a stack
# we will use pop()
print(myStack.pop())
print(myStack)

# demo 2
myStack2 = []

myStack2.append(30.1)
myStack2.append(40.1)
myStack2.append(50)
myStack2.append(60.1)
myStack2.append(70.1)
myStack2.append(80)

# demo of other functions associated with stack
# empty()
