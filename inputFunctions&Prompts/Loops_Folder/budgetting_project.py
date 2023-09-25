#budgetting project
#income
salary = int(input("Enter your income: "))
sidehustle = int(input("Enter your additional income: "))

#expenses
utilityBills = int(input("Enter your utility expense: "))
grocery = int(input("Enter your grocery expense: "))
allowance = int(input("Enter your allowance: "))

#Goals
goal1 = 'Improve my tech set up'
goal2 = 'Go on a vacation'
goal3 = 'Start a business'
goal4 = 'Education bills'
myGoal = goal1

#use if elif for logic
if (myGoal == goal1):
    newIncome = salary + sidehustle
    if(newIncome >= 40000):
        expense_net = newIncome * 50/100
        allowance_net = newIncome * 30/100
        savings_net = newIncome * 20/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif(newIncome >= 50000):
        expense_net = newIncome * 30/100
        allowance_net = newIncome * 30/100
        savings_net = newIncome * 30/100
        leisure_net = newIncome * 10/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry, your income category is not listed")

elif(myGoal == goal2):
    newIncome = salary + sidehustle
    if(newIncome >= 40000):
        expense_net = newIncome * 50/100
        allowance_net = newIncome * 30/100
        savings_net = newIncome * 20/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif(newIncome >= 50000):
        expense_net = newIncome * 30/100
        allowance_net = newIncome * 30/100
        savings_net = newIncome * 30/100
        leisure_net = newIncome * 10/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry, your income category is not listed")

elif(myGoal == goal3):
    newIncome = salary + sidehustle
    if(newIncome >= 40000):
        expense_net = newIncome * 50/100
        allowance_net = newIncome * 30/100
        savings_net = newIncome * 20/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif(newIncome >= 50000):
        expense_net = newIncome * 30/100
        allowance_net = newIncome * 30/100
        savings_net = newIncome * 30/100
        leisure_net = newIncome * 10/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry, your income category is not listed")

else:
    newIncome = salary + sidehustle
    if(newIncome >= 40000):
        expense_net = newIncome * 50/100
        allowance_net = newIncome * 30/100
        savings_net = newIncome * 20/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)

    elif(newIncome >= 50000):
        expense_net = newIncome * 30/100
        allowance_net = newIncome * 30/100
        savings_net = newIncome * 30/100
        leisure_net = newIncome * 10/100

        print(expense_net)
        print(allowance_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry, your income category is not listed")

print("my goal is ", goal2)
