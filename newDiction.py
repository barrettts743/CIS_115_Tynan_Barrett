#create a dictionary that contains at least 3 objects
names_addresses = [{
    "firstName": "John",
    "lastName": "Doe",
    "city": "New York",
    "state": "NY",
    "zipCode": "10001",
    "phoneNumber": "123-456-7890"
    },
    {
    "firstName2": "Jane",
    "lastName2": "Smith",
    "city2": "Los Angeles",
    "state2": "CA",
    "zipCode2": "90001",
    "phoneNumber2": "987-654-3210"
    },
    {
    "firstName3": "Alice",
    "lastName3": "Johnson",
    "city3": "Chicago",
    "state3": "IL",
    "zipCode3": "60601",
    "phoneNumber3": "555-123-4567"
    }] 

#create a function for user to input new entries
def print_dictionary():
    "firstName" = input("Enter First Name: ")
    'lastName' = input("Enter Last Name: ")
    'city' = input("Enter City: ")
    'state' = input("Enter State: ")
    'zipCode' = input("Enter Zip Code: ")
    'phoneNumber' = input("Enter Phone Number: ")
    

#print the dictionary
print_dictionary(names_addresses)
