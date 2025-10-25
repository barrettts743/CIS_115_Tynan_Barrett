

student_grades = "grades"
myDictionary = {student_grades: [input("Enter grade 1: "),
                                 input("Enter grade 2: "), 
                                 input("Enter grade 3: "),
                                 input("Enter grade 4: "),
                                 input("Enter grade 5: ")
                                ]}
def calculate_average(grades):
    total = 0
    for grade in grades:
        total += float(grade)
    average = total / len(grades)
    return average

def print_result(myDictionary):
    grades = myDictionary[student_grades]
    average = calculate_average(grades)
    print(f"The average grade is: {average:.2f}")
    return

print_result(myDictionary)