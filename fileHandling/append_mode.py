# in append we add new statements to the text file
# learning how thenappend function works

var_name = open("file1.txt", "a")

var_name.write("I can't find my pen")
var_name.write("I miss my desk")
var_name.write("I miss my previous huse")

var_name.close()

with open("file1.txt") as file_read:
    text = file_read.read()
print(text)
