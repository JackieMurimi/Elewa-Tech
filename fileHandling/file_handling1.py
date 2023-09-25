# We are going to write operations
# read,write, append

# write
var_name = open("statements.txt", "w")

var_name.write("The teacher wants us to do this on our own\n")
var_name.write("The teacher wants us to do this on our own\n")
var_name.write("The teacher wants us to do this on our own\n")

var_name.close()
# read
with open("statements.txt") as file_read:
    text = file_read.read()
print(text)

# append
var_name = open("statements.txt", "a")

var_name.write("The class is almost over\n")
var_name.write("Today was a long day\n")
var_name.write("so, that's it\n")

var_name.close()

with open("statements.txt") as file_read:
    text = file_read.read()
print(text)
