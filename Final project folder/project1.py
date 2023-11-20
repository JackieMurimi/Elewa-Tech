# Child Planning Program to determine if one is ready for another child

def calculate_expenses(current_children, future_child):
    # Simulated expenses for a child
    monthly_expense_per_child = 800
    total_children = current_children + future_child
    total_monthly_expenses = total_children * monthly_expense_per_child
    return total_monthly_expenses

def can_afford_another_child(current_children):
    monthly_income = float(input("Enter your monthly income: "))
    current_expenses = float(input("Enter your current monthly expenses: "))
    
    future_child = 1
    while True:
        total_expenses = calculate_expenses(current_children, future_child)
        total_monthly_expenses = current_expenses + total_expenses
        
        print(f"\nIf you have {current_children} child(ren) now and plan to have {current_children + future_child} child(ren) in the future:")
        print(f"Total monthly expenses would be: ${total_monthly_expenses}")
        
        if total_monthly_expenses <= 0.6 * monthly_income:  # Checks if expenses are less than 60% of income
            print("Congratulations! You can afford another child.")
            break
        else:
            decision = input("You might have financial difficulties. Do you want to reconsider having another child? (yes/no): ")
            if decision.lower() == 'no':
                break
            else:
                future_child += 1

def main():
    current_children = int(input("Enter the number of children you currently have: "))
    can_afford_another_child(current_children)

if __name__ == "__main__":
    main()

