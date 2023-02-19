choice = input('May I have a piece of candy? (yes/no) ').lower() == 'no'

if choice:
    while choice:
        choice = input('May I have a piece of candy ').lower() == 'no'
        if not choice:
            print('Thank you. ')
            break
        
else:
    print('Thank you ')