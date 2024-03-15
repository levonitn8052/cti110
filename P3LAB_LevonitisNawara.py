# Nawara Levonitis

# 03/14/2024

# P3LAB

# LAB: Leap year

is_leap_year = False

input_year = int(input())

#divided by 400 and divided by 100 gives leap yer
if (input_year % 400 == 0 and input_year % 100 == 0):
    print(input_year, '- leap year')
    
#divided by 4 and not divided by 100 gives leap year    
elif (input_year % 4 == 0 and input_year % 100 != 0):
        print(input_year, '- leap year')
        
#not divided by both 400 and 4 gives not leap year
else:
    print(input_year, '- not a leap year')
