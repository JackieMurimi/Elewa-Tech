# this is a demo of how to create stacks from a module
# the module being used is called deque
# the module also holds the methods that we use to get information about a stack

# imports
from collections import deque

myStack = deque()
# append()
myStack.append("1")
myStack.append("2")
myStack.append("3")
myStack.append("4")
myStack.append("5")
myStack.append("6")

# print(myStack.empty())
print(myStack.getSize())
