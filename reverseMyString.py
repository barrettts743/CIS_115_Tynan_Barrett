#this program will reverse a string input by the user
#define function
def reverseMyString(word):
    reversedWord = word[::-1]
    return reversedWord

#define main function
def main():
    #get user input
    userInput = input('Enter a string: ')
    print(f'You entered:', userInput)
    #call function
    result = reverseMyString(userInput)
    print(f'Your reversed string is:', result)
#call main function
main()