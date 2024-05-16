# Nawara Levonitis

# 03/05/2024

# P2HW2

# Creating the list of grades

 
# Enter grades
Module_1 = float(input("Enter grade for Module 1: ")) 
Module_2 = float(input("Enter grade for Module 2: "))
Module_3 = float(input("Enter grade for Module 3: "))
Module_4 = float(input("Enter grade for Module 4: "))
Module_5 = float(input("Enter grade for Module 5: "))
Module_6 = float(input("Enter grade for Module 6: "))

# The List of grades
List_Grades = [Module_1, Module_2, Module_3, Module_4, Module_5, Module_6]

print()

# Print the result of grades 
print("------- Results -------")

# The lowest grade in the list
print(f'Lowest Grade:     {min(List_Grades):.2f}')

# The highest grade in the list
print(f'Highest Grade:    {max(List_Grades):.2f}')

# Sum of grades
print(f'Sum of Grades:    {sum(List_Grades):.2f}')

# The average of grades 
print(f'Average:          {sum(List_Grades)/6:.2f}')

print("-------------------------------")



