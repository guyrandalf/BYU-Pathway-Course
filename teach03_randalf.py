meal_price_per_child = float(input('What is the price of a child\'s meal? '))
meal_price_per_adult = float(input('What is the price of an adult\'s meal? '))
no_of_child = int(input('How many children are there? '))
no_of_adult = int(input('How many adults are there? '))
sales_tax = float(input('What is the sales tax rate? '))
child_total = meal_price_per_child * no_of_child
adult_total = meal_price_per_adult * no_of_adult
sub_total = child_total + adult_total
print()
print(f'Subtotal: ${round(sub_total, 2)}')