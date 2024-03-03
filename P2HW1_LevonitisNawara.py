 # Nawara Levonitis

 # 03/02/2024

 # P2HW1

 # Change from P1HW2 assignment

 
print("This program calculates and displays travel expenses")

# Enter travel budge
Travel_Budget = float(input("Enter Budget: ")) 

# Enter travel destination
Travel_Destination = input("Enter your travel destination: ")

# Enter gas estimation
Travel_Gas = float(input("How much do you think you will spend on gas? ")) 

# Enter accomodation estimation
Travel_Hotel = float(input("Approximately, how much will you need for accommodation/hotel? ")) 

# Enter Food budget 
Travel_Food = float(input("Last, how much do you need for food? ")) 

# Add all travel expenses
Total_Expense = (Travel_Gas+Travel_Hotel+Travel_Food)

print()
 
print("------- Travel Expenses -------")

# Print travel destination, budget and travel expenses
print("Location:        ", Travel_Destination)
print(f'Initial Budget:   ${Travel_Budget:.2f}')
print(f'Fuel:             ${Travel_Gas:.2f}')
print(f'Accomodation:     ${Travel_Hotel:.2f}')
print(f'Food:             ${Travel_Food:.2f}')
print("-------------------------------")

print()

# Print remaining balance, substract expenses from budget 
print(f'Remaining Balance: ${Travel_Budget-Total_Expense:.2f}')

