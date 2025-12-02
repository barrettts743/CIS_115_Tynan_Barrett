#this is capture users credit card.

card_number = input('Enter your credit card number: ')
expiration_date = input('Enter your card expiration date (MM/YY): ')
CVV = input('Enter your CVV number: ')

#print info back to user.
print(f'The credit card number you entered is {card_number}')
print(f'The expiration date on this card is {expiration_date}')
print(f'The CVV number on this card is {CVV}')
