# Nawara Levonitis

# 03/18/2024

# P3HW2

# This program displays an employee's salary information


# Enter name of employee
Employee_name = input("Enter emloyee's name: ")

# Enter number of hours worked
Num_hour_worked = float(input('Enter number of hours worked: '))

# Enter employee's pay rate
Employee_pay_rate = float(input("Enter employee's pay rate: "))

# Evaluate employee's overtime and pay
OverTime_hour = Num_hour_worked - 40
if Num_hour_worked > 40:
    Overtime_pay = Employee_pay_rate * 1.5 * OverTime_hour
else:
    Overtime_pay = 0
    
print('-----------------------------------------')

# Output employee's name
print('Employee name:  ', Employee_name)

print('')

# detarmine pay information, regular hour pay and gross pay 
Regular_pay = Employee_pay_rate * 40
Gross_pay = Regular_pay + Overtime_pay

# Ouput the header
print('Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay')
print('----------------------------------------------------------------------------------')

# Out put the results
print(f'{Num_hour_worked:<16.1f}{Employee_pay_rate:<12.2f}{OverTime_hour:<12.1f}{Overtime_pay:<16.2f}${Regular_pay:<15.2f}${Gross_pay:<15.2f}')









