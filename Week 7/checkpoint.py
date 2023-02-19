number = float(input('Please type a positive number. '))

if number <= 0:

    while number <= 0:
        number = float(input(' Enter a positive number '))
        if number >= 0:
            print('The number is {number:.0f}')
            break

else:
    print(f'number is {number:.0f}')