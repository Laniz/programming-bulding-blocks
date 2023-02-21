colors = ["red", "blue", "green", "yellow"]

count = 0

for i in colors:
    print(f'the color is {i}')
    count += 1
print(f'they were {count} colors in the list')

print(' ')

count1 = 0
for number in range(1, 9):
    print(f'the number is {number}')
    count1 += 1
print(f'There are {number} numbers')

print(' ')

for numbers in range(2, 21, 2):
    print(numbers)

print(' ')

first_name = 'shepherd'
for index, letter in enumerate(first_name):
    print(f'The letter is {letter.capitalize()} it is at position {index + 1}')