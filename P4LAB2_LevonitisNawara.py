# Nawara Levonitis

# 04/02/2024

# P4LAB2

# LAB: Output Range with increment of 5

# Define variable names
Num_one = int(input())
Num_two = int(input())

# If the second integer is less than the first integer
if Num_one > Num_two: 
    print("Second integer can't be less than the first.",end='')

#  While first integer is less than or equal to the second integer    
while Num_one <= Num_two:
    print(Num_one,end=' ') 
    Num_one += 5
    
# Output with a newline 
print()
    
