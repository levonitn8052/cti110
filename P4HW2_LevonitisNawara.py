# Nawara Levonitis

# 04/13/2024

# P4HW2

# This program displays an employee's salary information and some calculations


Num = 0
Num_overtime = 0
Num_reghours = 0
Num_gross = 0
Employee_name = ''

# Loop to collect employee's name
while Employee_name != 'Done':

    # Enter name of employee
    Employee_name = input("Enter emloyee's name or 'Done' to tereminate: ")

    # When it is terminated, output the result, otherwise continue to collecct information
    if Employee_name == 'Done':
        print('')
        print('Total number of employee entered:', Num)
        print(f'Total amount paid for overtime: ${Num_overtime:.2f}')
        print(f'Total amount paird for regular hours: ${Num_reghours:.2f}')
        print(f'Total amount paid in gross: ${Num_gross:.2f}')
    else:
  
        # Enter number of hours worked
        Num_hour_worked = float(input(f'How many hours did {Employee_name} work? '))

        # Enter employee's pay rate
        Employee_pay_rate = float(input(f"What is {Employee_name}'s pay rate? "))

        # Evaluate employee's overtime and pay
        if Num_hour_worked > 40:
            OverTime_hour = Num_hour_worked - 40
            Overtime_pay = Employee_pay_rate * 1.5 * OverTime_hour
        else:
            OverTime_hour = 0
            Overtime_pay = 0
            
        # Output employee's name
        print('')
        print('Employee name:  ', Employee_name)
        print('')

        # detarmine pay information, regular hour pay and gross pay
        if Num_hour_worked < 40:
            Regular_pay = Employee_pay_rate * Num_hour_worked
        else:
            Regular_pay = Employee_pay_rate * 40
            
        Gross_pay = Regular_pay + Overtime_pay

        # Ouput the header
        print('Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay')
        print('----------------------------------------------------------------------------------')

        # Out put the results
        print(f'{Num_hour_worked:<16.1f}{Employee_pay_rate:<12.2f}{OverTime_hour:<12.1f}{Overtime_pay:<16.2f}${Regular_pay:<15.2f}${Gross_pay:<15.2f}')
        print('')

        # Increment the results
        Num += 1
        Num_overtime +=  Overtime_pay
        Num_reghours += Regular_pay
        Num_gross += Gross_pay    
    







