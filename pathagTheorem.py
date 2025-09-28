#this program will calculate the hypotenuse of a right triangle
#using the Pythagorean Theorem
import math

#define functions
def calculate_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

#define main function
def main():
    #get user input
    side_a = float(input('Enter the length of side a: '))
    print(f'You entered:', side_a)
    side_b = float(input('Enter the length of side b: '))
    print(f'You entered:', side_b)
    #call the function
    hypotenuse = calculate_hypotenuse(side_a, side_b)
    print(f'The length of the hypotenuse is:', hypotenuse)

#call main function
main()
