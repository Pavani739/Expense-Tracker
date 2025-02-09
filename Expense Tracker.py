import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.file_name = "expenses.json"
        self.load_expenses()
    
    def load_expenses(self):
        try:
            with open(self.file_name, "r") as file:
                self.expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []
    
    def save_expenses(self):
        with open(self.file_name, "w") as file:
            json.dump(self.expenses, file, indent=4)
    
    def add_expense(self):
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter category (Food, Entertainment, Utilities, etc.): ")
        amount = float(input("Enter amount spent: "))
        self.expenses.append({"date": date, "category": category, "amount": amount})
        self.save_expenses()
        print("Expense added successfully!\n")
    
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.\n")
            return
        print("Date         | Category      | Amount")
        print("-----------------------------------")
        for exp in self.expenses:
            print(f"{exp['date']} | {exp['category']:<12} | ${exp['amount']:.2f}")
        print()
    
    def summary(self):
        if not self.expenses:
            print("No expenses recorded.\n")
            return
        total = sum(exp['amount'] for exp in self.expenses)
        avg = total / len(self.expenses)
        category_totals = {}
        for exp in self.expenses:
            category_totals[exp['category']] = category_totals.get(exp['category'], 0) + exp['amount']
        
        print(f"Total Expenses: ${total:.2f}")
        print(f"Average Expense: ${avg:.2f}")
        print("Expenses by Category:")
        for category, amount in category_totals.items():
            print(f"  {category}: ${amount:.2f}")
        print()
    
    def run(self):
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Summary")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.summary()
            elif choice == '4':
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    ExpenseTracker().run()
