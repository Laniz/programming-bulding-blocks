first_opt_br_two_one = input('enter')


count = 0
while first_opt_br_two_one.lower() != 'open sesame':
    count += 1
    print(f'"You have {5 - count} atempts left! ')
    password = input('What is the password')
    if count == 5:  
        if count == 4:
            print('game over')
        break
                