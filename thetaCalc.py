#this program will calculate the angle theta in a right triangle
#using the atan2 function from the math module
import math

#define function
def calculate_theta(y, x):
    #acquire radian and convert to degree
    theta_radian = math.atan2(y, x)
    theta_degree = theta_radian*(180/math.pi)
    print(f'The angle in degrees is:', theta_degree)
    return theta_degree

#define main function
def main():
    #get user input
    y = float(input(f'Enter the length of the side y to angle theta: '))
    print('You entered:', y)
    x = float(input(f'Enter the length of the side x to angle theta: '))
    print(f'You entered:', x)
    #call the function
    calculate_theta(y, x)

#call main function
main()