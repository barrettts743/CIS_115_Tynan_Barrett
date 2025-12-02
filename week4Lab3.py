#this program allows user use % to determine if operation is even or odd.
#grab 2 numbers from user
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

#assign variable to hold total value through division.
dividend = num1 // num2

#Get the remainder of num1 divided by num2.
remainder = dividend % 2

#determine if total is even or odd.
if remainder % 2 == 0:
    print('Even')

else:
    print('Odd')