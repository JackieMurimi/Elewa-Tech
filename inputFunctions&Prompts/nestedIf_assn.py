# You are supposed to run an errand in the bank. Write a pseudocode that will represent your wholesome decision 
#to go to the bank, run the errand of your choice and perform the mini-activities you want to perform in the bank. 
#Afterwards convert that into python code
weather = "Sunny"
network = "down"
mall_shopping = "yes"

if(weather == "Sunny"):
    if(network == "down"):
        print("You need to go to the bank")
    elif(mall_shopping == "no"):
        print("call the bank for assistance")
    else:
        print("Be patient and try again after an hour")

#You are the one to prepare your small sibling to go back to school. 
#Given that the shopping budget you have is sh.35000, describe how you will get to decide what 
#to buy for your small sibling as they go back to school in a pseudocode. 
#Finally convert that into python code.
budget = 35000
term_length = "9 weeks"
visitting_day = 1

if(budget == 35000):
    if(term_length == "9 weeks"):
        print("Buy all the items in the shopping list")
    elif(visitting_day == 1):
        print("Only buy items to last till the visitting day")
    else:
        print("Just shop")




#You are the chair of an event committee set to have an event on the 29th day of August. 
#Describe to us in a pseudocode how you will get to decide the flow of events or activities in that particular event. 
#Then convert that into python code.

event_day = "29th"
pledges = "fulfilled"
venue = "booked"
decor = "set"
caterer = "prebooked"

if(event_day == "29th"):
    if(pledges == "fulfilled"):
        if(venue == "booked"):
            print("We are ready to get the decor done")
    elif(caterer == "not booked"):
        print("we need to prioritize food")
    else:
        if(decor == "set"):
            if(caterer == "prebooked"):
                print("We are all set, time to celebrate")
