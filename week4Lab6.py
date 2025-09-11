#this program will print an address to the user.
#Grab an address from the user.
address = input('Enter your Street Address: ')
city = input('Enter your city: ')
state = input('Enter your state: ')
zip_code = input('Enter your zip code: ')

#combine the address in a string variable.
full_address = (f'{address}\n{city}, {state}\n{zip_code}')

#display the address to the user.
print(f'The address you entered is: \n{full_address}')

#this is the end of the program.
input('Press Enter to close...')
