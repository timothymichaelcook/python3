#VARIABLES DECLARED HERE:
lovely_loveseat_description = "Item 1: Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.\n"

lovely_loveseat_price = 254.00

stylish_settee_description = "Item 2:Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.\n"

stylish_settee_price = 180.50

luxurious_lamp_description = "Item 3: Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.\n"

luxurious_lamp_price = 52.15

sales_tax = 0.088

customer_one_total = 0

customer_one_itemization = ""

#SHOPPING CART CALCULATED HERE
customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

#TOTAL & TAX OF PURCHASE CALCULATED HERE
customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

#OUTPUT OF EXPRESSIONS HERE
print("Items purchased:")
print(customer_one_itemization)
print("Customer One Total:")
print(round(customer_one_total, 2))

