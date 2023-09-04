#I will update what this is about
#goal is not to be hungry

food = [3, 2 , 1] #food is present
exhausted = 3  #if they reach level 5 of exhaustion they will not cook
guests = 5  #this will be part of the else() block

for i in food:
    exhausted = exhausted + 1
    if(exhausted > 3):
        print("you can buy food")
    else:
       print("Go to the kitchen and cook")

else:
    if(guests >= 5):
        print("go buy some food")
    else:
        print("go prepare some food")