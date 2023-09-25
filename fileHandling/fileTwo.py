# today we are learning file handling
# learning how to read,write and append operations
# we'll have three different operations

# casestudy one - read mode
'''var_name = open("file1.txt", "r")
for each in var_name:
    print(each)'''

# print(var_name)


# read mode second demo
file_read = open("file1.txt", "r")
print(file_read.read())


# third demo
with open("file1.txt") as file_read:
    text = file_read.read()
print(text)

# split operations on text
with open("file1.txt", "r") as data:
    data_1 = data.readlines()
    for line in data_1:
        var = line.split()
        print(var)
