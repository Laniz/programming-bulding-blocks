print('Welcome to the Shopping Cart Program!')
print(' ')

items_list = []

prices_list = []

choice = ''

item = ''

price = 0

counter = 0

sum_total = 0

while choice != 5:
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    print(' ')

    choice = int(input('Please enter an action: '))
    
    if choice == 1:
        item = input('What item would you like to add? ')
        price = float(input(f'What is the price of {item}? $' ))
        counter += 1

        sum_total += price

        items_list.append(item)
        prices_list.append(price)

        print(f'"{item}" has been added to cart')
        print(' ')

    if choice == 2:
        print(' ')
        print('The contents of the shopping cart are:')
        print(' ')

        for i, (x, y) in enumerate(zip(items_list, prices_list)):          
            print(f"{i+1}. {x.capitalize()} - ${y:.2f}")
            print(' ')

    if choice == 3:     
        remove_number = int(input('Which item would you like to remove? '))
        index_number = remove_number - 1

        print(' ')
        confrim = input(f'Are you sure you want to remove {items_list[index_number]} (y/n) ').lower() == 'y'


        if confrim:
            print('')
            
            items_list.pop(remove_number - 1)
            prices_list.pop(remove_number - 1)
            
            print('Item has been removed')

        if not confrim:
            print(' ')
            print('Item was not removed')


    if choice == 4:

      print(f'The total price of the items in the shopping cart is ${sum_total:.2f}')
       
            
            

