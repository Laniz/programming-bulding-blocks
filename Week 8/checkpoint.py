colors = ["red", "blue", "green", "yellow"]

count = 0

for i in colors:
    print(f'the color is {i}')
    count += 1
print(f'they were {count} colors in the list')

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(' ')
count1 = 0
for number in range(1, 9):
    print(f'the number is {number}')
    count1 += 1
print(f'There are {number} numbers')


for numbers in range(2, 21, 2):
    print(numbers)