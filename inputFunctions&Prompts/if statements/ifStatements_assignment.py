#Shopping scenario. 
#Write a code that will help you to decide the budget of the things you want to go shopping for and 
#determine how many items you get to buy with that budget.
item_one = "diapers at 1800"
item_two = "cerelac at 450"
item_three = "biscuits at 300"
budget = 2300

if(budget <= 2300):
    print("Buy ", item_one, "and ", item_two)
else:
    print("Buy ", item_one, item_two, "and ", item_three)

#Career scenario. Write a code that will help you decide on what will influence your career choice.
career_path = "science based"
salary_estimate = "high"

if(career_path == "science based" and salary_estimate == "high"):
    print("You found the career of your dreams")
else:
    print("Keep searching")


#Gifting Scenario. 
#Write a code that will help you find the best gift to give someone who has done 
#something that impressed you or made you want to gift them.
gift_one = "fully paid vacation"
gift_two = "movie ticket"
gift_three = "spa voucher"
satisfaction_level = "very happy"

if(satisfaction_level == "very happy"):
    print("You just got a ", gift_one)
else:
    print("Here's a ", gift_three, "to go unwind")
