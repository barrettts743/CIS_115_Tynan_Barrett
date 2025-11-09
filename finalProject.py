#create array of dictionaries to hold details of inventory catalog
inventory_data = [
        {"product_id: 1", "SKU: usb_k981", "price: 12.00", "description: USB 128 GB drive", "qoh: 1000"},
        {"product_id: 2", "SKU: mbpro_490", "price: 2900.00", "description: Mac Book Pro 15 inch", "qoh: 45"},
        {"product_id: 3", "SKU: chip_1010", "price: 48.00", "description: Arduino microprocessor", "qoh: 325"},
        {"product_id: 4", "SKU: cam_78", "price: 156.00", "description: Ring Camera Model 78", "qoh: 98"},
        {"product_id: 5", "SKU: smt_tv_100", "price: 359.00", "description: TCL Smart TV", "qoh: 225"}
        ]
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
selected_product = int(input("Enter the Product ID of the item you wish to purchase: "))
selected_quantity = int(input("Enter the quantity you wish to purchase: "))
#confirm quantity is available in inventory
available_qoh = (list(inventory_data[selected_product - 1])[4].split(": ")[1])
print("-" * 40)
#confirm shopper selection
print(f"You have selected {selected_quantity} {shopper_catalog[selected_product]}.")
print("-" * 40)
#prompt shopper to confirm purchase
confirm_purchase = input("Do you wish to confirm your purchase? (yes/no): ").strip().lower()
if confirm_purchase != 'yes':
    print("Purchase cancelled.")
    print("-" * 40)
    exit()
else:
    print("Purchase confirmed.")
    print("Please proceed to checkout.")
print("-" * 40)
#ask for shopper billing/shipping information
print("Please enter your billing and shipping information.")
first_name = input("First Name: ")
last_name = input("Last Name: ")
address = input("Address: ")
city = input("City: ")
state = input("State: ")
zip_code = input("Zip Code: ")
#store shopper information in dictionary
shopper_info = {
    "first_name": first_name,
    "last_name": last_name,
    "address": address,
    "city": city,
    "state": state,
    "zip_code": zip_code
}
print("-" * 40)
#proceed to have shopper enter payment details
print("Please enter your payment details.")
card_number = input("Card Number: ")
expiry_date = input("Expiry Date (MM/YY): ")
cvv = input("CVV: ")
#calculate total cost of shopper selection
item_price_str = shopper_catalog[selected_product].split(" - $")[1]
item_price = float(item_price_str)
total_cost = item_price * selected_quantity
print(f"Your total cost is: ${total_cost:.2f}")
print("-" * 40)