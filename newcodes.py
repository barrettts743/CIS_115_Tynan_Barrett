#create dictionary for inventory catalog
inventory_data = [
        {"product id: 1", "SKU: usb_k981", "price: 12.00", "description: USB 128 GB drive", "qoh: 1000"},
        {"product id: 2", "SKU: mbpro_490", "price: 2900.00", "description: Mac Book Pro 15 inch", "qoh: 45"},
        {"product id: 3", "SKU: chip_1010", "price: 48.00", "description: Arduino microprocessor", "qoh: 325"},
        {"product id: 4", "SKU: cam_78", "price: 156.00", "description: Ring Camera Model 78", "qoh: 98"},
        {"product id: 5", "SKU: smt_tv_100", "price: 359.00", "description: TCL Smart TV", "qoh: 225"}
        ]
#create header for shopper
print("-" * 40)
print("Product Catalog" .center(40))
print("-" * 40)
#print inventory catalog in without displaying Sku, and QoH
for item in inventory_data:
    item_list = list(item)
    product_id = item_list[0].split(": ")[1]
    price = item_list[2].split(": ")[1]
    description = item_list[3].split(": ")[1]
    print(f"Product ID: {product_id} | Description: {description} | Price: ${price}")
print("-" * 40)
#display the catalog to shopper




#prompt shopper to select item by product ID
selected_product = input("Please enter the product ID of the item you wish to purchase: ")
#confirm selection
print(f"You have selected product ID: {selected_product}. Thank you for your selection!")
#create dictionary for inventory catalog








