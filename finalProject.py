#dictionary for product catalog
product_catalog = {
    "USB DRIVE(128 GB): $12.00",
    "Mac Book Pro(15 inch): $2900.00",
    "Arduino 1010(with bluetooth): $48.00",
    "Ring Camera(wireless): $156.00",
    "Smart TV(TCL 70 inch): $359.00"
    }
print("-" * 40)
print("Product Catalog" .center(40))
print("-" * 40)
#display the product catalog
for product in product_catalog:
    print(product)

#create new dictionary to store product ID, SKU, price and quantity on hand
inventory_data = {
    1: {"SKU": usb_k981, "price": 12.00, "qoh": 1000},
    2: {"SKU": mbpro_490, "price": 2900.00, "qoh": 45}
    3: {"SKU":  },
}
#create empty dictionary to store user options
shopping_cart = {}