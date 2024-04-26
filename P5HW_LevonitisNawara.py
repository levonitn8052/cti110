#Nawara Levonitis

#4/25/24

#P5HW

#simple math quizzes program


# Import a library to generate random numbers
import random

# Create an empty list
type_history =[]

print('Welcome to Math Quiz')
print('')
print('')


# Define Main Menu
def menu():
    print('MAIN MENU')
    print('----------------------')
    print('1. Adding Random Numbers')
    print('2. Substracting Random Numbers')
    print('3. Exit')
    print('')
    Menu_num = int(input('Please choose one of the menu options: '))
    # Addition
    if Menu_num == 1:
        addition()
    # Substraction
    elif Menu_num == 2:
        substruction()
    # Termination    
    elif Menu_num == 3:
        print('Thank you for playing...\nBye!!\n')
        exit
    else:
        print('Enter valid number\n')
        menu()

# Define the addition
def addition():
    # Rest a list
    type_history =[]
    
    ran_1 = random.randint (0, 300)
    ran_2 = random.randint (0, 300)
    right_num = ran_1 + ran_2
    print(" ", ran_1)
    print("+" , ran_2)
    print('')
    user_text = int(input('Enter answer.\n'))

    while right_num != user_text:
        if right_num == user_text:
            print('Congratulations!!!! Your answer is correct.')
            print('')
            menu()
        else:
            if right_num > user_text:
                print ("Sorry, guess is too low.")
                print('')
                type_history.append(user_text)
                user_text = int(input('Try again: '))
            elif right_num < user_text:
                print ("Sorry, guess is too high.")
                print('')
                type_history.append(user_text)
                user_text = int(input('Try again: '))
                
    if right_num == user_text:
        print('Congratulations!!!! Your answer is correct.')
        print('Number of guesses: ', len(type_history)+1)
        print('')
        menu()  

# Define the substruction
def substruction():
    # Rest a list
    type_history =[]
    
    ran_1 = random.randint (0, 300)
    ran_2 = random.randint (0, 300)
    right_num = ran_1 - ran_2
    print(" ", ran_1)
    print("-", ran_2)
    print('')
    user_text = int(input('Enter answer.\n'))

    while right_num != user_text:
        if right_num == user_text:
            print('Congratulations!!!! Your answer is correct.')
            print('')
            menu()
        else:
            if right_num > user_text:
                print ("Sorry, guess is too low.")
                print('')
                type_history.append(user_text)
                user_text = int(input('Try again: '))
            elif right_num < user_text:
                print ("Sorry, guess is too high.")
                print('')
                type_history.append(user_text)
                user_text = int(input('Try again: ')) 

    if right_num == user_text:
        print('Congratulations!!!! Your answer is correct.')
        print('Number of guesses: ', len(type_history)+1)
        print('')
        menu() 

            
print('')

# Call menu
menu()

print('')





