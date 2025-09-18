#this program allows user to enter 10 grade
gradesEntered = input('How many grades do you want to enter? ')

#enter grade
grade = input('Enter grade: ')

for gradesEntered in range(int(gradesEntered)):
    grade = input('Enter grade: ')
    print('You entered: ' + grade)
    gradesEntered = gradesEntered + 1
print('You entered ' + str(gradesEntered) + ' grades.')
