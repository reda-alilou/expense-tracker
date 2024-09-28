def add_expense():
    date = input('enter the date of the expenses (in the format YYYY-MM-DD): ')
    category = input('enter the Description of the expense: ')
    description = input('enter the category of the expenses: ')
    amount = input('enter the amount spent: ')
    
    with open('expenses.csv', 'a') as file:
        file.write(f"{date},{category},{description},{amount}\n")

def view_expenses():
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
        if len(lines) <= 1:
            print('No expenses recorded yet!')
        else:
            Date, Category, Description, Amount = 'Date', 'Category', 'Description', 'Amount'
            print(f'{Date:<10} | {Category:<15} | {Description:<15} | {Amount}')
            print('-' * 50)
            for line in lines[1:]:
                date, category,  description, amount = line.strip().split(',')
                print(f'{date:<10} | {category:<15} | {description:<15} | {amount}')

def edit_expense():
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
    if len(lines) <= 1:
        print('No expenses recorded yet!')
    else:
        for index, line in enumerate(lines[1:], start=1):
            date, category, description, amount = line.strip().split(',')
            print(f'{index}. {date:<10} | {category:<15} | {description:<15} | {amount}')
        choice_to_modify = input('choose the line to modify: ')
        if choice_to_modify.isdigit() and 1 <= int(choice_to_modify) <= len(lines) - 1:
            new_date = input('New date: ')
            new_category = input('New category: ')
            new_description = input('New description: ')
            new_amount = input('New amount')
            lines[int(choice_to_modify)] = f'{new_date},{new_category},{new_description},{new_amount}\n'
        else:
            print('Please enter a valid number!')
            edit_expense()
        with open('expenses.csv', 'w') as file:
            file.writelines(lines)

def delete_expense():
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
    if len(lines) <= 1:
        print('No expenses recorded yet!')
    else:
        for index, line in enumerate(lines[1:], start=1):
            date, category, description, amount = line.strip().split(',')
            print(f'{index}. {date:<10} | {category:<15} | {description:<15} | {amount}')
        choice_to_delete = input('choose the line to delete: ')
        if choice_to_delete.isdigit() and 1 <= int(choice_to_delete) <= len(lines) - 1:
            lines.pop(int(choice_to_delete))
            print("Expense deleted successfully!")
        else:
            print('Please enter a valid number!')
            delete_expense()
        with open('expenses.csv', 'w') as file:
            file.writelines(lines)

def view_summary():
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
        if len(lines) <= 1:
            print('No expenses recorded yet!')
        else:
            total_amount_spent = 0
            category_totals = {}
            for line in lines[1:]:
                date, category,  description, amount = line.strip().split(',')
                total_amount_spent += float(amount)
                if category in category_totals:
                    category_totals[category] += float(amount)
                else:
                    category_totals[category] = float(amount)
            print('The total amount spent is: ', round(total_amount_spent, 2))
            print('The total spent per category is: ')
            Category, Total, Percentage = 'Category', 'Total', 'Percentage'
            print(f'{Category:15} | {Total:<15} | {Percentage}')
            print('-' * 50)
            for category, total in category_totals.items():
                percentage = round((total / total_amount_spent) * 100, 2)
                print(f'{category:<15} | {total:<15,.2f} | {percentage}%')

def main():
    while True:
        choice = input('1. Add a new expense \n2. View all expenses \n3. Edit an expense \n4. Delete an expense \n5. View expense Summary \n6. Exit\n')
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            edit_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            view_summary()
        elif choice == '6':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Please choose a number between 1 and 6!')

if __name__ == "__main__":
    main()