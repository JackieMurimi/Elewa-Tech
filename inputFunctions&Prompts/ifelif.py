#illustration of if  elif statements
#the syntax is 
#if(criteria):
#    statements
#elif(criteria):
#    statements
#else:
#     statements
#first example
#university awarding process scenario

attendance = 45
points = 65
co_curricular = 15

if(attendance >= 35):
    print("You are an excellent student")
elif(points >= 60):
    print("You are a performing student")
elif(co_curricular >= 5):
    print("You are an active student")
else:
    print("You are a below average student")

#second example
#shoes shopping
baby_one = "Ethan"
baby_two = "Ashley"

shoeSize_one = 34
shoeSize_two = 28

shoeType_one = "Sports"
shoeType_two = "Ngoma"

budget_one = 5000
budget_two = 3500

if(baby_one == "Ethan" and baby_two == "Ashley"):
    print("proceed to shop")
elif(shoeSize_one == 34):
    print("Ethan's shoe shopping")
elif(shoeSize_two == 28):
    print("Ashley's shoe shopping")
elif(shoeType_one == "Sports"):
    print("Ethan's right selection")
elif(shoeType_two == "Bgoma"):
    print("Ashley's right selection")
elif(budget_one == 5500 and budget_two == 5000):
    print("let's do this!")
else:
    print("This is not working")


#no powwer scenario
power = 0
training = 3
assn = 1

if(power == 1):
    print("We have class")
elif(training == 0):
    print("postpone class")
elif(training == 1):
    print("Give assignment")
else:
    print("assign take home")
