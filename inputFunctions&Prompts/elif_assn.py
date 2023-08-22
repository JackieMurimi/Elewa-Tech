# Imagine you are about to prepare dinner, you have only a budget of sh. 1500, 
#write a pseudocode that will help you decide on what to buy to fit your budget 
#after deciding what you will have for super. Then convert it to python code

beans = 600
chapati = 400
beef = 1200
ugali = 400
budget = 1500

if(budget == 1500):
    print("Buy beans and chapati")
elif(beef <= 1200):
    print("Buy beef and eat tumbukiza")
else:
    print("Buy ugali and beans")

#You are about to purchase a ticket for something or some chilling over the weekend. 
#You have to decide whether you will attend the movies or you’ll go for sport. 
#Write a pseudocode that will take you through the steps of deciding what you will do and how much you will spend. 
#Then convert that into a python code.

weekend_plan = "chill"
weather_1 = "chilly"
weather_2 = "sunny"

if(weather_1 == "chilly"):
    print("Go to the movies")
elif(weather_2 == "sunny"):
    print("Go sporting")
else:
    print("grab some drinks and netflix at home")


#You are about to do some cleaning in your house. You have a lot to do. 
#Write a pseudocode that will represent how you will perform your cleaning from the first chore to the last. 
#Then convert it into a python code.

energy_levels = "high"
cleaning_load = "heavy"
time = "limited"

if(cleaning_load == "heavy" and time == "limited"):
    print("Load the washing machine and start cleaning the house")
elif(energy_levels == "high" and cleaning_load == "light"):
    print("handwash and get your adrenaline up")
else:
    print("automate everything and save time")