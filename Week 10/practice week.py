fruits = ['lemon', 'grape', 'cherry', 'banana', 'apple']

print(fruits)
print(' ')

print(fruits.sort())
print(' ')

fruits.remove('cherry')
print(fruits)
print(' ')

fruits.insert(2, 'melon')
print(fruits)
print(' ') 

position = fruits.index('lemon')
print(f'lemon was found at position {position}')
print(' ')