# Function to add a new expense entry
def add_expense():
    # Collecting the expense details from the user
    date = input('Enter the date of the expenses (in the format YYYY-MM-DD): ')
    category = input('Enter the category of the expense: ')
    description = input('Enter the description of the expenses: ')
    amount = input('Enter the amount spent: ')
    
    # Append the entered expense details to the 'expenses.csv' file
    with open('expenses.csv', 'a') as file:
        file.write(f"{date},{category},{description},{amount}\n")

# Function to display all recorded expenses
def view_expenses():
    # Open the CSV file in read mode
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
        
        # Check if there are any expenses recorded
        if len(lines) <= 1:
            print('No expenses recorded yet!')
        else:
            # Print the table header
            Date, Category, Description, Amount = 'Date', 'Category', 'Description', 'Amount'
            print(f'{Date:<10} | {Category:<15} | {Description:<15} | {Amount}')
            print('-' * 50)
            
            # Iterate through each recorded expense and display it in a formatted manner
            for line in lines[1:]:
                date, category, description, amount = line.strip().split(',')
                print(f'{date:<10} | {category:<15} | {description:<15} | {amount}')

# Function to edit an existing expense entry
def edit_expense():
    # Read all lines from the CSV file
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
        
    # Check if there are any expenses to edit
    if len(lines) <= 1:
        print('No expenses recorded yet!')
    else:
        # Display all expenses with an index for selection
        for index, line in enumerate(lines[1:], start=1):
            date, category, description, amount = line.strip().split(',')
            print(f'{index}. {date:<10} | {category:<15} | {description:<15} | {amount}')
        
        # Prompt the user to choose which expense to edit
        choice_to_modify = input('Choose the line to modify: ')
        
        # Validate the user's choice
        if choice_to_modify.isdigit() and 1 <= int(choice_to_modify) <= len(lines) - 1:
            # Collect the updated expense details from the user
            new_date = input('New date: ')
            new_category = input('New category: ')
            new_description = input('New description: ')
            new_amount = input('New amount: ')
            
            # Update the selected expense line with the new details
            lines[int(choice_to_modify)] = f'{new_date},{new_category},{new_description},{new_amount}\n'
        else:
            print('Please enter a valid number!')
            edit_expense()  # Recursively call the function again for another attempt
            
        # Write the updated lines back to the CSV file
        with open('expenses.csv', 'w') as file:
            file.writelines(lines)

# Function to delete an existing expense entry
def delete_expense():
    # Read all lines from the CSV file
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
        
    # Check if there are any expenses to delete
    if len(lines) <= 1:
        print('No expenses recorded yet!')
    else:
        # Display all expenses with an index for selection
        for index, line in enumerate(lines[1:], start=1):
            date, category, description, amount = line.strip().split(',')
            print(f'{index}. {date:<10} | {category:<15} | {description:<15} | {amount}')
        
        # Prompt the user to choose which expense to delete
        choice_to_delete = input('Choose the line to delete: ')
        
        # Validate the user's choice
        if choice_to_delete.isdigit() and 1 <= int(choice_to_delete) <= len(lines) - 1:
            # Remove the selected expense from the list
            lines.pop(int(choice_to_delete))
            print("Expense deleted successfully!")
        else:
            print('Please enter a valid number!')
            delete_expense()  # Recursively call the function again for another attempt
            
        # Write the updated lines back to the CSV file
        with open('expenses.csv', 'w') as file:
            file.writelines(lines)

# Function to display a summary of expenses
def view_summary():
    # Read all lines from the CSV file
    with open('expenses.csv', 'r') as file:
        lines = file.readlines()
        
    # Check if there are any expenses to summarize
    if len(lines) <= 1:
        print('No expenses recorded yet!')
    else:
        total_amount_spent = 0  # Initialize the total amount spent
        category_totals = {}    # Initialize a dictionary to store totals per category
        
        # Iterate through each expense to calculate the total and category-wise spending
        for line in lines[1:]:
            date, category, description, amount = line.strip().split(',')
            total_amount_spent += float(amount)
            
            # Add to the category total or initialize it if it doesn't exist
            if category in category_totals:
                category_totals[category] += float(amount)
            else:
                category_totals[category] = float(amount)
        
        # Display the total amount spent
        print('The total amount spent is: ', round(total_amount_spent, 2))
        
        # Display the spending per category with percentages
        print('The total spent per category is: ')
        Category, Total, Percentage = 'Category', 'Total', 'Percentage'
        print(f'{Category:15} | {Total:<15} | {Percentage}')
        print('-' * 50)
        
        # Calculate and display each category's total and percentage contribution
        for category, total in category_totals.items():
            percentage = round((total / total_amount_spent) * 100, 2)
            print(f'{category:<15} | {total:<15,.2f} | {percentage}%')

# Main function to run the program and display the menu
def main():
    while True:
        # Display the menu options
        choice = input('1. Add a new expense \n2. View all expenses \n3. Edit an expense \n4. Delete an expense \n5. View expense Summary \n6. Exit\n')
        
        # Execute the corresponding function based on user input
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

# Entry point of the program
if __name__ == "__main__":
    main()