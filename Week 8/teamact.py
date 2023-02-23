variable = 'commitment'
variable2 = 'commitmens'
# variable_len = len(variable)
# fav_let = input('What is your favourite letter? ')

# for letter in variable:
#     print(letter, end="") 

# #end="-" adds dashes to thr end of the line

letter = input('Enter a letter ')

found = False

index = 0

# while index < len(variable) and not found:
#     if letter == variable[index]:
#         found = True
#     else:
#         index += 1


# if not found:
#     print(f'{letter} was not found in {variable}')
    
# else:
#     (print(f'{}'))

index = variable.find(letter)
if index == -1:
    print(f'{letter} was not found in {variable} at position {index}')

else:
    print(f'{letter} was not found in {variable}' )



#comparing two strings


for index, letter in enumerate(variable):
    if letter == variable2[index]:
        print(f'{letter} {index}')
