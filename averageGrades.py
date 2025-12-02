#this program calculates the average of five grades entered by a user

#create the dictionary to hold the grade as well as the student name
student_grades = {}

#prompt the user for the student's name and grades to store in the dictionary
for i in range(5):
    name = input(f'Enter the name of student {i + 1}: ')
    grade = float(input(f"Enter the grade for {name}: "))
    student_grades[name] = grade

#function to calculate the average grade
def calulate_average_grade(grades_dict):
    total = 0
    for grade in grades_dict.values():
        total += grade
    average = total / len(grades_dict)
    return average

#function to print the result
average = calulate_average_grade(student_grades)
print(f"The average grade for the entered students is: {average:.2f}")
