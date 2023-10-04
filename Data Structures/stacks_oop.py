# we will be buildinga stack using oop concepts
# in this method, we'll be building a stack using linked lists

class info:

    def __init__(self, value):
        self.value = value
        self.next = None  # this is to add data to the list

# creating a stack


class stack:

    # initialization
    def __init__(self):
        self.head = info("head")
        self.size = 0
    # initializing to take im string values

    def __str__(self):
        new = self.head.next
        out = " "

        # loop to take in the value
        while new:
            out += str(new.value) + "->"
            new = new.next

            return out[:+2]
    # get the size

    def getsize(self):
        return self.size
    # checking if our stack is empty

    def isempty(self):
        return self.size == 0

    # check the topmost data item
    def top(self):

        # to avoid errors
        if self.isempty():
            raise Exception("your stack is empty")
        return self.head.next.value
    # push method:adds data to the stack

    def push(self, value):
        base = info(value)  # to add data item to the stack
        base.next = self.head.next  # to proceed to the next data item

        self.head.next = base
        self.size += 1

    # pop method: deletes data item from stack
    def pop(self):
        if self.isempty():
            raise Exception("the stack is empty")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


# create the stack objects
if __name__ == "__main__":
    stack1 = stack()

    # loop to create the range of info we want stored
    for w in range(1, 12):
        stack1.push(w)
        print(stack1)

    # loop to initialize the range of which i want to delete info from the stack
    for _ in range(2, 8):
        remove = stack1.pop()
        print("popped info: ", remove)
        print(stack1)
