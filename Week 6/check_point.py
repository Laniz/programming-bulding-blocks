print('Enter the following on a scale of 1 t0 10\n')

loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history '))
income = int(input('How high is your income? '))
down_payment = int(input('How big is your down payment? '))
print(' ')


can_load = False

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        can_load = True
    
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            can_load = True
        else:
            can_load = False

    else:
        can_load = False

elif loan_size < 5:
    if credit_history < 4:
        can_load = False
    elif income >= 7 or down_payment >= 7:
        can_load = True
    elif income >= 4 and down_payment >= 4:
        can_load = True
    else:
        can_load = False

if can_load:
    print('Loan has been aprroved')
else:
    print('You are not approved')
