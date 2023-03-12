checking = []
savings = []
emergency_funds = []
choice = ''
count = 0
sum_1 = 0
sum_2 = 0
sum_3 = 0


print(' ')
print(choice)
print(' ')
while choice != 'quit':
    print('Enter the names and balances of bank accounts (type: quit when done) ')
    choice = input('What is the name of this account? ')
    count += 1
    print(' ')
    print(choice)
    print(' ')

    if choice.lower() == 'checking':
        checking_amount = float(input('What is the balance? '))

        sum_1 += checking_amount
        checking.append(checking_amount)

    elif choice.lower() == 'savings':
        savings_amount = float(input('What is the balance? '))

        sum_2 += savings_amount
        savings.append(savings_amount)

    elif choice.lower() == 'emergency fund':
        emergency_funds_amount = float(input('What is the balance? '))

        sum_3 += emergency_funds_amount
        emergency_funds.append(emergency_funds_amount)

print('Account Information:')
print(f'checking - ${sum_1:.2f}')
print(' ')
print(f'savings - ${sum_2:.2f}')
print(' ')
print(f'emergency fund - {sum_3:.2f}')
print(' ')

total = sum_1 + sum_2 + sum_3
average = total / 3

print(f'Total: ${total:.2f}')
print(f'Average: ${average:.2f}')
