print('Welcome to our store, please enter the following information. \n')
print('---------------------------------------------------------\n')

#used " for the next two lines instead of my normal '
child_meal = input("What is the price of a child's meal? $")
adult_meal = input("What is the price of a adult's meal? $")
number_of_children = input('How many children are there? ')
number_of_adults = input('How many adults are there? ')
drinks = input('How many drinks are there? ')
sales_tax_rate = input('What is the sales tax? ')
tip = input('what is the tip percentage? ')

#subtotal = childmeal price x number of children plus adult meal price times number of adults
child_adult_total = float(child_meal) * int(number_of_children) + float(adult_meal) * int(number_of_adults)
drinks_grand_total = 1.99 * int(drinks)
subtotal = drinks_grand_total + child_adult_total

#calculating the tip, not sure if tips are taxed, am leaving them untaxed.
tip_in_money = subtotal * (float(tip) / 100)

#sales tax
sales_tax = (float(sales_tax_rate) * subtotal) / 100
total = subtotal + sales_tax

#tip that will be printed for the customer.
tip_in_money = total * (int(tip) / 100)
#grand total for everything!!
grand_total = tip_in_money + total 

#print output
print('  ')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Tip: ${tip_in_money:.2f}')
print(f'Sales tax: ${sales_tax:.2f}')
print(f'Total: ${grand_total:.2f}\n')

#calculating the change
payment_amount = input('What is the payment amount? $')
change = float(payment_amount) - total

print(f'Change: ${change:.2f} \n')
print('---------------------------------------------------------\n')
print('Thank you for shopping with us! \n')