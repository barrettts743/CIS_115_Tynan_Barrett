#create a dictionary that contains at least 3 objects
names_addresses = [{
    "firstName": "Johnny",
    "lastName": "Holler",
    "city": "Vancouver",
    "state": "BC",
    "zipCode": "10001",
    "phoneNumber": "123-456-7890"
    },
    {
    "firstName2": "Bobby",
    "lastName2": "Smith",
    "city2": "Los Angeles",
    "state2": "CA",
    "zipCode2": "90001",
    "phoneNumber2": "987-654-3210"
    },
    {
    "firstName3": "Clayton",
    "lastName3": "Prince",
    "city3": "Des Moines",
    "state3": "IA",
    "zipCode3": "60601",
    "phoneNumber3": "555-123-4567"
    }] 

#create user defined function
def print_dictionary(names_addresses):
    for entry in names_addresses:
        print(entry)


#print the dictionary
print_dictionary(names_addresses)






added_items == 'n':
print(input('Would you like to check out (y or n)?: '))
if input == 'y':
            print("Proceeding to checkout...")
    else:
            print("Returning to shopping cart...")
            print("-" * 40)
    return