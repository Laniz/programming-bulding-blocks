# Compute the sum, or total, of the numbers in the list.

# Compute the average of the numbers in the list.

# Find the maximum, or largest, number in the list.

number_list = []
number = -1
counter = 0
sum = 0
print('Enter a list of numbers, type 0 when finished.')
while number != 0:
    number = int(input('Enter a number '))
    counter += 1
    print(f'the counter is {counter}')

    if number != 0:
        number_list.append(number)
        sum = sum + number
        print(f'the sum is {sum}')

average = sum / (counter - 1)

print(f'The sum is {sum}')
print(f'The average is {average}')
print(f'The largest number is {max(number_list)}')
print(f'The smallest number is {min(number_list)}')

