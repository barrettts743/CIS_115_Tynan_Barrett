#this program uses looping to grab an number from user and determine if it is in a certain range

def main():
    #grab user input
    num = int(input("Enter a number between 1 and 100: "))

    #use while loop to determine if number is in range
    while num < 1 or num > 100:
        print("The number you entered is out of range. Please try again.")
        num = int(input("Enter a number between 1 and 100: "))

    #print out end statement
    print(f'The number you entered is {num}, which is in range. Thank you!')
    