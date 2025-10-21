def userMain():
    print_dictionary()
    print_result(myDictionary)
    print(myDictionary[])
    return

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
    
#calling print_result function to print each value from myDictionary
def print_result(myDictionary[]):
    print("First Name: ", myDictionary[0])
    print("Last Name: ", myDictionary[1])
    print("City: ", myDictionary[2])
    print("State: ", myDictionary[3])
    print("Zip Code: ", myDictionary[4])
    print("Phone Number: ", myDictionary[5])