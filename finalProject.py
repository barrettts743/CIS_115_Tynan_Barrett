#create array of dictionaries to hold details of inventory catalog
shopping_data = [
    {"product_id": 1, "sku": "usb_k981", "price": 12.00, "description": "USB 128 GB drive", "qoh": 1000},
    {"product_id": 2, "sku": "mbpro_490", "price": 2900.00, "description": "Mac Book Pro 15 inch", "qoh": 45},
    {"product_id": 3, "sku": "chip_1010", "price": 48.00, "description": "Arduino microprocessor", "qoh": 325},
    {"product_id": 4, "sku": "cam_78", "price": 156.00, "description": "Ring Camera Model 78", "qoh": 98},
    {"product_id": 5, "sku": "smt_tv_100", "price": 359.00, "description": "TCL Smart TV", "qoh": 225},
]
#create new dictionary to hold formatted inventory details for shopper
shopper_catalog = {item['product_id']: f"{item['description']} - ${item['price']:.2f}" for item in shopping_data}

#shopping cart to hold shopper selections
shopping_cart = []

#inventory data 
inventory_data = {item['product_id']: item['qoh'] for item in shopping_data}

#create prompt for shopper to view product catalog and select item by product ID 
print("-" * 40)
print("Product Catalog" .center(40))
print("-" * 40)
for product_id, details in shopper_catalog.items():
    print(f"{product_id} | {details}")
print("-" * 40)

#prompt shopper to select item by product ID and the quantity desired
selected_product = int(input(f"Enter the Product ID of the item you wish to purchase: "))
selected_quantity = int(input(f'Enter the quantity you would like to purchase: '))
<<<<<<< Updated upstream
#Check the quantity of the selected product is available in inventory
if selected_quantity > inventory_data[selected_product]:
    print(f"Sorry, only {inventory_data[selected_product]} of {shopper_catalog[selected_product]} available.")
    selected_quantity = inventory_data[selected_product]

#shopper selection added to shopping cart
shopping_cart.append ({
    'product_id': selected_product,
    'quantity': selected_quantity
})
#confirm shopper selection
print(f"You have selected {selected_quantity} of {shopper_catalog[selected_product]}.")
print("-" * 40)

#promt user if they would like to add anymore items to their shopping cart and the quantity desired
def added_items():
    while True:
        add_more = input('Would you like to add another item (y or n)?: ')
        if add_more == 'y':
            new_product = int(input(f"Enter the Product ID of the item you wish to purchase: "))
            new_quantity = int(input(f'Enter the quantity you would like to purchase: '))
            #Check the quantity of the selected product is available in inventory
            if new_quantity > inventory_data[new_product]:
                print(f"Sorry, only {inventory_data[new_product]} of {shopper_catalog[new_product]} available.")
                new_quantity = inventory_data[new_product]

            #add items to shopping cart
            shopping_cart.append ({
            'product_id': new_product,
            'quantity': new_quantity
            })
        
            print(f"{new_quantity} of {shopper_catalog[new_product]} has been added to your shopping cart.")
            print("-" * 40)

        elif add_more == 'n':
            checkout = input('Would you like to check out (y or n)?: ')
            
            if checkout == 'y':
                print("Proceeding to checkout...")
                total_cost()
                break
            else:
                print("Returning to shopping cart...")
                print("-" * 40)
    return
=======
#store shopper selection in shopping cart dictionary
shopping_cart = [
    {'product_id': selected_product},
    {'quantity': selected_quantity}
]
#confirm shopper selection
print(f"You have selected {selected_quantity} of {shopper_catalog[selected_product]}.")
print("-" * 40)
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
        return True
if available_qoh():
    print(f"{selected_quantity} of {shopper_catalog[selected_product]} has been added to your shopping cart.")
print("-" * 40)

#promt user if they would like to add anymore items to their shopping cart and the quantity desired
def added_items():
    added_items = input('Would you like to add another item (y or n)?: ')
    if added_items == 'y':
            #prompt user to a new item to shopping cart and store selection in shopping cart dictionary
            new_product = int(input(f"Enter the Product ID of the item you wish to add: "))
            new_quantity = int(input(f'Enter the quantity you would like to add: '))
            #check the quantity of the selected product is available in inventory
            if new_quantity > inventory_data[new_product - 1]['qoh']:
                print(f"Sorry, we only have {inventory_data[new_product - 1]['qoh']} of {shopper_catalog[new_product]} available.")
                return added_items()
            #store additional item selection in shopping cart dictionary
            shopping_cart.append({'product_id': new_product})
            shopping_cart.append({'quantity': new_quantity})
            print(f"You have selected {new_quantity} of {shopper_catalog[new_product]}.")
            print(f"{new_quantity} of {shopper_catalog[new_product]} has been added to your shopping cart.")
    print("-" * 40)
    if added_items == 'n':
        print(input('Would you like to check out (y or n)?: '))
        if input == 'y':
            print("Proceeding to checkout...")
        else:
            print("Returning to shopping cart...")
            return
added_items()
>>>>>>> Stashed changes


#calculate total cost of all shopper's selected items
def total_cost():
<<<<<<< Updated upstream
    total_cost = 0.0

    for item in shopping_cart:
        product_id = item['product_id']
        quantity = item['quantity']
        price = float(shopper_catalog[product_id].split(" - $")[1])
        total_item = price * quantity
        total_cost += total_item
    print(f"Your total cost is: ${total_cost:.2f}")
=======
    item_price_str = shopper_catalog[selected_product].split(" - $")
    item_price_str = item_price_str[1]
    item_price = float(item_price_str)
    total_cost = item_price * selected_quantity
    print(f"The total cost of your order is: ${total_cost:.2f}")
>>>>>>> Stashed changes
    print("-" * 40)
added_items()
#ask for shopper billing/shipping information
#dictionary for shopper information
shopper_info = {
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'address': 'Address',
    'city': 'City',
    'state': 'State',
    'zip_code': 'Zip Code',
    'email': 'Email',
    'phone': 'Phone Number'
}
#shopper information prompts
print("Please enter your billing and shipping information.")    
first_name = input("First Name: ")
last_name = input("Last Name: ")
address = input("Address: ")
city = input("City: ")
state = input("State: ")
zip_code = input("Zip Code: ")
email = input("Email: ")
phone = input("Phone Number: ")
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
print(f"Email: {email}")
print(f"Phone: {phone}")
total = 0.0
for item in shopping_cart:
    product_id = item['product_id']
    quantity = item['quantity']
    item_price = float(shopper_catalog[product_id].split(" - $")[1])
    total_item = item_price * quantity
    print(f"{shopper_catalog[product_id]} | Quantity: {quantity} | Item Total: ${total_item:.2f}")
    total += total_item
print(f"Total Cost: ${total:.2f}")
print("-" * 40)
print("Thank you for your purchase! Your order has been confirmed.")
print("-" * 40)

