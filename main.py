
import json
from pathlib import Path

# File where transactions will be saved
data_file = Path(__file__).with_name("transactions.json")

# Load previously saved transactions
if data_file.exists():
    with open(data_file, "r") as file:
        transactions = json.load(file)
else:
    transactions = []

# Calculate balance from saved transactions
balance = 0.0

for transaction in transactions:
    if transaction["type"] == "income":
        balance += transaction["amount"]
    else:
        balance -= transaction["amount"]

print("Welcome to my Finance Tracker!")


while True:
    print("\nMain Menu")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transaction History")
    print("5. View Spending Summary")
    print("6. Exit")


    
    choice = input("\nChoose an option (1-6): ")


    if choice == "1":

        
        try:
            income = float(input("Enter income amount (£): "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue

        if income <= 0:
            print("Income must be greater than £0.")
            continue


        transactions.append({
            "type": "income",
            "amount": income
        })

        with open(data_file, "w") as file:
            json.dump(transactions, file, indent=4)

        print(f"Income added: £{income:.2f}")

    
    elif choice == "2":
        
        try:
            expense = float(input("Enter expense amount (£): "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue

        if expense <= 0:
            print("Expense must be greater than £0.")
            continue

        
        valid_categories = ["Food", "Transport", "Shopping", "Bills", "Other"]

        while True:
            category = input("Enter category: ").strip().title()

            if category in valid_categories:
                break
            else:
                print("Invalid category!")
                print("Choose: Food, Transport, Shopping, Bills, Other")


        balance -= expense

        transactions.append({
            "type": "expense",
            "amount": expense,
            "category": category
        })

        with open(data_file, "w") as file:
            json.dump(transactions, file, indent=4)

        print(f"Expense added: £{expense:.2f}")
        print(f"Category: {category}")

    
    elif choice == "3":
        print(f"Current Balance: £{balance:.2f}")

    elif choice == "4":
        print("\nTransaction History")

        if not transactions:
            print("No transactions recorded yet.")
        else:
            for number, transaction in enumerate(transactions, start=1):
                transaction_type = transaction["type"].capitalize()
                amount = transaction["amount"]

                
                if transaction["type"] == "expense":
                    category = transaction.get("category", "Uncategorised")
                    print(f"{number}. Expense: £{amount:.2f} | Category: {category}")
                else:
                    print(f"{number}. Income: £{amount:.2f}")


   
    elif choice == "5":
        print("\nSpending Summary")

        totals = {}

        for transaction in transactions:
            if transaction["type"] == "expense":
                category = transaction.get("category", "Uncategorised").title()
                amount = transaction["amount"]

                totals[category] = totals.get(category, 0) + amount

        if totals:
            for category, total in totals.items():
                print(f"{category}: £{total:.2f}")
        else:
            print("No expenses recorded yet.")

    elif choice == "6":
        print("Goodbye! Thanks for using Finance Tracker.")
        break

    else:
        print("Invalid option. Please choose 1-6.")


