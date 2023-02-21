firstname = 'shepherd'
letter_count = 7

firstname_len = len(firstname)

# for index in range(letter_count):
#     print(f'the letter at position {index} is {firstname[index]}' )



# for index in range(firstname_len):
#     print(f'the letter at position {index} is {firstname[index]}' )


for index, letter in enumerate(firstname):
    print(f' the letter {letter} is at {index}')