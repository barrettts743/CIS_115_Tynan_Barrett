#create the array of dictionaries
name_and_addresses = {
    "firstName": [],
    "lastName": [],
    "city": [],
    "state": [],
    "zipCode": [],
    "phoneNumber": []
}

#function to add information to the dictionary
def add_entry(firstName, lastName, city, state, zipCode, phoneNumber):
    name_and_addresses["firstName"].append(firstName)
    name_and_addresses["lastName"].append(lastName)
    name_and_addresses["city"].append(city)
    name_and_addresses["state"].append(state)
    name_and_addresses["zipCode"].append(zipCode)
    name_and_addresses["phoneNumber"].append(phoneNumber)

#function to print the dictionary
def print_dictionary(dictionary):
    #the format for printing the dictionary
    for i in range(len(dictionary['firstName'])):
            print(f'Entry {i + 1}:')
            print(f"First Name: {dictionary['firstName'][i]}")
            print(f"Last Name: {dictionary['lastName'][i]}")
            print(f"City: {dictionary['city'][i]}")
            print(f"State: {dictionary['state'][i]}")
            print(f"Zip Code: {dictionary['zipCode'][i]}")
            print(f"Phone Number: {dictionary['phoneNumber'][i]}")

#gather information for up to 3 entries
for i in range(3):
    print(f'Person {i + 1}:')
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    zipCode = input("Enter Zip Code: ")
    phoneNumber = input("Enter Phone Number: ")
    add_entry(firstName, lastName, city, state, zipCode, phoneNumber)

#call the function to print the dictionary
print_dictionary(name_and_addresses)