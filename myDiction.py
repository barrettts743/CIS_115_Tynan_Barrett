def userMain():
    print_dictionary()

#grab user information and store it in a dictionary

def print_dictionary():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zipCode = input("Enter your zip code: ")
    phoneNumber = input("Enter your phone number: ")
    myDictionary = [firstName, lastName, city, state, zipCode, phoneNumber]
    return myDictionary
    
#print any result from myDictionary
