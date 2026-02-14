# Status -> In Progress: Implemented a calcluation mechanism but still have to figure out tax and pre-tax tip addition amount and spliting between freinds mechnaism

'''
Problem Description:
Create a program that helps a group of friends split a restaurant bill fairly, considering different scenarios like unequal orders, shared items, and custom tip percentages.

    Group: 4 people (Alice, Bob, Carol, Dave)

    Individual Orders:
    - Alice: Pasta ($15.99), Soda ($2.50)
    - Bob: Burger ($12.99), Beer ($6.00)
    - Carol: Salad ($11.50), Water ($0.00)
    - Dave: Steak ($24.99), Wine ($8.00)

    Shared Items:
    - Nachos ($12.00) - split among all 4
    - Cheesecake ($8.00) - split between Alice & Bob only

    Tax: 8%
    Tip: 18% (on pre-tax amount)
'''

order_dict = {
    'pasta': 15.99,
    'soda': 2.50,
    'burger': 12.99,
    'beer': 6.00,
    'salad': 11.50,
    'water': 0.00,
    'steak': 24.99,
    'wine': 8.00,
    'nachos': 12.00,
    'cheesecake': 8.00
}

customer_order = list()
customer_num = int(input("Enter a number of customers: "))
print()
for i in range(customer_num):
    istr = f"How many order a there for {i+1} customer : "
    items_num = int(input(istr))
    items_order = list()
    for j in range(items_num):
        jstr = f"Enter the {j+1} item purchased: " 
        items_order.append(input(jstr).lower())
    customer_order.append(items_order)
    print()

tip = float(input("Enter a tip amount(%): "))

customer_total = list()
for customer in customer_order:
    total = 0
    for items in customer:
        total += order_dict[items]
    customer_total.append(round(total, 2))

print()
print("Total:")
for total in customer_total:
    print(f"Total of {customer_total.index(total)+1} is customer: {total}")
