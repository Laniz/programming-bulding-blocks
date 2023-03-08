#creating variables I will need later.
items_list = []
prices_list = []
choice = ''
item = ''
price = 0
counter = 0
sum_total = 0

#print statements for welcome
print('Welcome to the Shopping Cart Program!')
print(' ')

#fuction for printing out the menu
def menu_list_items():
    print('Please select one of the following:')
    print(' ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    print(' ')

#fuction for printing the contains of the cart
def print_shopping_cart_content():
    print(' ')
    print('The contents of the shopping cart are:')
    print(' ')

    for i, (x, y) in enumerate(zip(items_list, prices_list)):          
        print(f"{i+1}. {x.capitalize()} - ${y:.2f}")
        print(' ')

#start of the of the loop    
while choice != 5:
    
    menu_list_items()

    #error checking the input for a interger
    while True:
        try:
            choice = int(input('Please enter an action: '))
            break

        except ValueError:
            print('Please enter a single digit number. (range 1 to 5)')
            print(' ')
            menu_list_items()
            print('')
    
    #add option
    if choice == 1:
        item = input('What item would you like to add? ')
        
        #error checking the input for float
        while True:
            try:
                price = float(input(f'What is the price of {item}? $' ))
                break

            except ValueError:
                print(' ')
                print('Please enter a numeric value for the price.')
                print(' ')

        #counter in case I need it
        counter += 1

        #total of the items in the shopping cart
        sum_total += price

        #addind items to both lists
        items_list.append(item)
        prices_list.append(price)

        print(f'"{item}" has been added to cart')
        print(' ')

    #view shopping cart
    if choice == 2:
        
        #this will check if list is currently empty, it will print different itmes depending on how many items are in the list.
        if len(items_list) == 0:

            print(' ')
            print('The shopping cart is currently empty.')
            print(' ')

        else:
            #call function to print
            print_shopping_cart_content()

    #remove item    
    if choice == 3:
        
        #function for printing shopping cart items
        print_shopping_cart_content()
     
        remove_number = int(input('Which item would you like to remove? '))

        #subtracting 1 from the user input 
        index_number = remove_number - 1

        #condition for removing items
        if remove_number >= 1 and remove_number <= (len(items_list) + 1):

            print(' ')
            confrim = input(f'Are you sure you want to remove {items_list[index_number]} (y/n): ').lower() == 'y'

            if confrim:
                print('')

                #removing items from the list.
                items_list.pop(index_number)
                prices_list.pop(index_number)
            
                print('Item has been removed')
                print(' ')

            if not confrim:
                print(' ')
                print('Item was not removed')

            # else:
            #     print(' ')
            #     print('Invaild input, item was not removed')
            #     print(' ')

        else:
            print('Sorry, that is not a valid item number.')

    if choice == 4:

      print(f'The total price of the items in the shopping cart is ${sum_total:.2f}')
      print(' ')

print('Thank you. Goodbye')
       
            
            

