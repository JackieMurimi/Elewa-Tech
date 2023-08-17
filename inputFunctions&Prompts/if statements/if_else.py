#if else statements

#school scenario
math = 78
physics = 80
eng = 73
chem = 82
marks = (math + physics + eng + chem)

if(marks >= 280):
    print(math)
    print(physics)
else:
    print(eng)

#house hunting scenario
house_a = 10000
house_b = 15000
budget = 12000

if(budget <= 12000):
    print(house_a)
    print("The rent is within the budget")
else:
    print(house_b)
    print("The rent is outside your budget")

    #baby scenario
    baby_age = 1

    if(baby_age >= "1 year"):
        print("Breastmilk is a must")
        print("The baby is still weaning")

#moving out scenario
school_dis = "near"
desire = " No freedom"

if(school_dis == "far" or desire == "freedom"):
    print("We are moving out")
else:
    print("Stay home")


