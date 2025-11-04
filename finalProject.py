inventory_data = [
     {"product": 1, "SKU": usb_k981, "price": 12.00, "description": USB 128 GB drive, "qoh": 1000},
     {"product": 2, "SKU": mbpro_490, "price": 2900.00, "description": Mac Book Pro 15 inch, "qoh": 45},
     {"product": 3, "SKU": chip_1010, "price": 48.00, "description": Arduino microprocessor, "qoh": 325},
     {"product": 4, "SKU": cam_78, "price": 156.00, "description": Ring Camera Model 78, "qoh": 98},
     {"product": 5, "SKU": smt_tv_100, "price": 359.00, "description": TCL Smart TV, "qoh": 225},
    ]

#dictionary for product catalog
product_catalog = {
    "USB DRIVE (128 GB): $12.00",
    "Mac Book Pro (15 inch): $2900.00",
    "Arduino 1010 (with bluetooth): $48.00",
    "Ring Camera (wireless): $156.00",
    "Smart TV (TCL 70 inch): $359.00"
    }
print("-" * 40)
print("Product Catalog" .center(40))
print("-" * 40)
#display the product catalog
for product in product_catalog:
    print(product)

#create empty dictionary to store user options
shopping_cart = {}
print(inventory_data)
