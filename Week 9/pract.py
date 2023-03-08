bark = True

while bark:
    print(' ')
    print('Do you want to bark of exit? ')
    bark = input('what is your choice ').lower() == 'bark'

    if bark:
        print(' ')
        print('You bark like a dog ')

    if not bark:
        print(' ')
        print('Enter a valid input ')
        

