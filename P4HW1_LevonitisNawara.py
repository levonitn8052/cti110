# Nawara Levonitis

# 04/11/2024

# P4HW1

# Creating the list of grades using a loop. Also, displaying score average and a letter grade for the calculated average.

 

# Collect number to enter
Num_Entry = int(input('How many scores do you want to enter? '))


# Collect the scores with numbers between 0 - 100
Score_List1 = []
num = 1

while num <= Num_Entry:
    Score_List1.append(float(input(f'Enter score #{num}: ')))

    # If the numner is not between 0 -100, ask user to enter again
    while (Score_List1[num-1] > 100 or Score_List1[num-1] < 0) :
        print('INVALID Score enteted!!!!')
        print('Score should be betweent 0 and 100')
        Score_List1.remove(Score_List1[num-1])
        Score_List1.append(float(input(f'Enter score #{num} again: ')))
    else:    
        num +=1

print()


# Print the result of grades 
print("---------- Results -----------")

# The lowest grade in the list
print(f'Lowest Score  : {min(Score_List1):.1f}')

# Drop the lowest grade
Score_List2 = []
i = 1
for i in range(len(Score_List1)):
    if Score_List1[i] == min(Score_List1):
        i += 1
    else:
        Score_List2.append(Score_List1[i])
        i += 1

    
# The List of grades
print(f'Modified List : {Score_List2}')

# The average of grades
avg = sum(Score_List2)/len(Score_List2)
print(f'Scores Average: {avg:.2f}')

# The final grade
if avg >= 90:
    print('Grade         : A')
elif avg >= 80:
    print('Grade         : B')
elif avg >= 70:
    print('Grade         : C')
elif avg >= 60:
    print('Grade         : D')
else:
    print('Grade         : F') 

print("-------------------------------")



