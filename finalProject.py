#create array of dictionaries to hold details of inventory catalog
shopping_data = [
    {"product_id": 1, "sku": "usb_k981", "price": 12.00, "description": "USB 128 GB drive", "qoh": 1000},
    {"product_id": 2, "sku": "mbpro_490", "price": 2900.00, "description": "Mac Book Pro 15 inch", "qoh": 45},
    {"product_id": 3, "sku": "chip_1010", "price": 48.00, "description": "Arduino microprocessor", "qoh": 325},
    {"product_id": 4, "sku": "cam_78", "price": 156.00, "description": "Ring Camera Model 78", "qoh": 98},
    {"product_id": 5, "sku": "smt_tv_100", "price": 359.00, "description": "TCL Smart TV", "qoh": 225},
]
#create shopping cart dictionary to hold shopper selection
shopping_cart = {}

#create new dictionary to hold formatted inventory details for shopper
shopper_catalog = {1: "USB 128 GB drive - $12.00",
                   2: "Mac Book Pro 15 inch - $2900.00",
                   3: "Arduino microprocessor - $48.00",
                   4: "Ring Camera Model 78 - $156.00",
                   5: "TCL Smart TV - $359.00"
                   }

#create prompt for shopper to view product catalog and select item by product ID 
print("-" * 40)
print("Product Catalog" .center(40))
print("-" * 40)
for product_id, details in shopper_catalog.items():
    print(f"{product_id} | {details}")
print()
print("-" * 40)

#prompt shopper to select item by product ID and the quantity desired
selected_product = int(input(f"Enter the Product ID of the item you wish to purchase: "))
selected_quantity = int(input(f'Enter the quantity you would like to purchase: '))
#confirm shopper selection
print(f"You have selected {selected_quantity} of {shopper_catalog[selected_product]}.")
print("-" * 40)
#create a dictionary to hold shopper selection
shopping_cart = {
    'product_id': selected_product,
    'quantity': selected_quantity
}
#check the quantity of the selected product is available in inventory
inventory_data = [
    {'product_id': 1, 'qoh': 1000},
    {'product_id': 2, 'qoh': 45},
    {'product_id': 3, 'qoh': 325},
    {'product_id': 4, 'qoh': 98},
    {'product_id': 5, 'qoh': 225},
]
def available_qoh():
    if selected_quantity > inventory_data[selected_product - 1]['qoh']:
        print(f"Sorry, we only have {inventory_data[selected_product - 1]['qoh']} of {shopper_catalog[selected_product]} available.")
        return False
    else:
        print(f"{selected_quantity} of {shopper_catalog[selected_product]} is available.")
        return True
if available_qoh():
    print(f"{selected_quantity} of {shopper_catalog[selected_product]} has been added to your shopping cart.")
print("-" * 40)

#promt user if they would like to add anymore items to their shopping cart and the quantity desired
def added_items():
    added_items = input('Would you like to add another item (y or n)?: ')
    if added_items == 'y':
        #add the new item and quantity to the shopping cart
        shopping_cart['product_id'] = input('What item would you like to add?: ')
        shopping_cart['quantity'] = input('Enter the quantity you would like to add?: ')
        print(f"{selected_quantity} of {shopper_catalog[selected_product]} has been added to your shopping cart.")
        print("-" * 40)
    if added_items == 'n':
        print(input('Would you like to check out (y or n)?: '))
        if input == 'y':
            print("Proceeding to checkout...")
    else:
            print("Returning to shopping cart...")
            print("-" * 40)
    return
added_items()


#calculate total cost of shopper selection
def total_cost():
    item_price_str = shopper_catalog[selected_product].split(" - $")
    item_price_str = item_price_str[1]
    item_price = float(item_price_str)
    total_cost = item_price * selected_quantity
    print(f"Your total cost is: ${total_cost:.2f}")
    print("-" * 40)
total_cost()

#ask for shopper billing/shipping information
#dictionary for shopper information
shopper_info = {
    'first_name': input("Enter your First Name: "),
    'last_name': input("Enter your Last Name: "),
    'address': input("Enter your address: "),
    'city': input("Enter your city: "),
    'state': input("Enter your state: "),
    'zip_code': input("Enter your zip code: "),
    'email': input("Enter your email: "),
    'phone': input("Enter your phone number: ")
}
print("Please enter your billing and shipping information.")    
first_name = input("First Name: ")
last_name = input("Last Name: ")
address = input("Address: ")
city = input("City: ")
state = input("State: ")
zip_code = input("Zip Code: ")
print("-" * 40)

#proceed to have shopper enter payment details
print("Please enter your payment details.")
#execute mod 10 check for cc number validation
def validateCreditCard(ccNum):
    ccNum = input("Enter your credit card number: ")
    oddDigits= []
    evenDigits = []
    total = 0
    #loop through the credit card number and separate the digits into odd and even lists
    for i in range(len(ccNum)-1, -1, -1):
        if (len(ccNum)-i) % 2 == 0:
            evenDigits.append(int(ccNum[i]))
        else:
            oddDigits.append(int(ccNum[i]))

    #double the even digits and if the result is greater than 9, subtract 9 from it
    for i in range(len(evenDigits)):
        evenDigits[i] = evenDigits[i] * 2
        if evenDigits[i] > 9:
            evenDigits[i] -= 9
    #sum all the digits in both lists
    total = sum(oddDigits) + sum(evenDigits)

    #determine if the credit card number is valid
    if total % 10 == 0:
        print('The credit card number is valid.')
    else:
        print('The credit card number is invalid. Please try again.')
        #invalid card retry
        return validateCreditCard(ccNum)
validateCreditCard('')
expiry_date = input("Expiry Date (MM/YY): ")
cvv = input("CVV: ")
#confirm purchase to user
print("Payment was successful.")
print("Here is your receipt.")

#create invoice receipt for customer that includes their details and order summary
print("-" * 40)
print("Invoice Receipt".center(40))
print("-" * 40)
print(f"Name: {first_name} {last_name}")
print(f"Address: {address}, {city}, {state} {zip_code}")
print(f"Product: {shopper_catalog[selected_product]}")
print(f"Quantity: {selected_quantity}")
item_price_str = shopper_catalog[selected_product].split(" - $")
item_price_str = item_price_str[1]
item_price = float(item_price_str)
total_cost = item_price * selected_quantity
print(f"Total Cost: ${total_cost:.2f}")
print("-" * 40)
print("Thank you for your purchase! Your order has been confirmed.")
print("-" * 40)




