 # Nawara Levonitis

 # 02/21/2024

 # P1HW2

 # It is a program that does some basic math on numbers that are entered.

 
print("This program calculates and displays travel expenses")

# Enter travel budget
Travel_Budget = int(input("Enter Budget: ")) 

# Enter travel destination
Travel_Destination = input("Enter your travel destination: ")

# Enter gas estimation
Travel_Gas = int(input("How much do you think you will spend on gas? ")) 

# Enter accomodation estimation
Travel_Hotel = int(input("Approximately, how much will you need for accommodation/hotel? ")) 

# Enter Food budget 
Travel_Food = int(input("Last, how much do you need for food? ")) 

# Add all travel expenses
Total_Expense = (Travel_Gas+Travel_Hotel+Travel_Food)
 
print("------- Travel Expenses -------")

# Print travel destination and budget
print("Location: ", Travel_Destination)
print("Initial Budget: ", Travel_Budget)
print("")

# Print travel expenses 
print("Fuel: ",Travel_Gas)
print("Accomodation: ", Travel_Hotel)
print("Food:", Travel_Food)
print("")

# Print remaining balance, substract expenses from budget 
print("Remaining Balance: ",Travel_Budget-Total_Expense)

