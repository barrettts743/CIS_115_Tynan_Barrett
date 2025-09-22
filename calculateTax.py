#this program allows user to calculate the salex for an item
#assign variables

item_price = 75.34
sales_tax_percent = 0.0725

#calculate the sales tax
sales_tax = item_price * sales_tax_percent

#calculate the total price of item
total_price = item_price + sales_tax

#print results
print('The item price is: ${:.2f}'.format(item_price))
print('The sales tax is: ${:.2f}'.format(sales_tax))
print('The total price is: ${:.2f}'.format(total_price))
