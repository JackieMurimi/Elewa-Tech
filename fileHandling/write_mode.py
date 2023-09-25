# second lesson in file handling
# we'll be writing using python in a txt file
# we'll be showcasing 3 different methods

# case study one
var_name = open("file1.txt", "w")

# writting inside the file starts here

var_name.write("Hello world")
var_name.write("My name is jackie")
var_name.write("This is the third statement")
var_name.write("Today is Monday")
var_name.write("I check my emails daily")

var_name.close()

with open("file1.txt") as file_read:
    text = file_read.read()
print(text)
