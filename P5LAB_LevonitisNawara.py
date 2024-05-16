# Nawara Levonitis

# 04/18/2024

# P5LAB

# Leap year - functions


def days_in_feb(user_year): 
    
    # check the year
    if user_year % 4 == 0 and user_year % 100 != 0:  
        return 29
    # if the century year
    elif user_year % 400 == 0:                      
        return 29
    # not a leap year
    else:                                           
        return 28
        
# print the result
if __name__ == '__main__':
    year = int(input())
    day = days_in_feb(int(year))
    print(f'{year} has {day} days in February.')
