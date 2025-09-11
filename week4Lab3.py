#this program allows user to input 3 integers 
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

#find the sum of num1 and num2
sum = int(num1) + int(num2)
total = int(sum)/int(num3)
print(total)

#determine if statement is greater than zero

if (total) >= 0:
    print('The mathematical operation is > 0')

else:
    print('The mathematical operation is <= 0')