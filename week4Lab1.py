#This program allows user to determine if their value is great than 0
#when divided by thier third value

num1 = input(int('Enter your first number: '))
num2  = input(int('Enter your second number:'))
num3 = input(int('Enter your third number: '))

#determine sum of first two numbers.
sum = num1 + num2
#divide sum by third number.
total = sum / num3
#determine if total is greater than 0.
if total > 0:
    print('The mathematical operation is > 0')

else:
    print('The mathematical operation is <= 0')
