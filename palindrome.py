#this program determines if the string input by user is a palindrome
#define function
def isPalindrome(word):
    return word == word[::-1]

#define main function    
def main():

#grab user input
    user_input = input('Enter a word of at least 5 characters: ')
    if len(user_input) < 5:
        user_input = input(f'Error. Enter word of at least 5 characters: ')
    else:
        print(f'You entered:', user_input)
    #check if palindrome
    if isPalindrome(user_input):
        print(f'Your word, {user_input}, is a palindrome.')
    else:
        print(f'Your word, {user_input}, is not a palindrome.')


#call main function
main()
