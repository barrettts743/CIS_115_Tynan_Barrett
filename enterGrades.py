#this program allows user to enter 10 grades
#assign number of grades to variable
x = 10

#assign variables
total = 0
count = 0
#use a while loop to get grades from user
while count < x:
    grade = float(input('Enter a grade: '))
    #print out each grade after user enters them
    print(f'You entered: {grade}')
    #add each grade to total
    total += grade
    count += 1

#Print out end statement
print(f' The user has entered {x} grades and is now done.')
