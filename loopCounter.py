#this program takes an integer input from the user and loops
#define functiom
def print_iteration(val):
    loopCounter = 0
    for i in range(val):
        loopCounter += 1
    return loopCounter

#define main function
def main():
    #grab user input
    userInput = int(input('Enter an integer: '))
    #call function
    result = print_iteration(userInput)
    print(f'The function call looped {result} times.')

#call main function
main()