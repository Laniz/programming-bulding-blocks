import random

rand_number = random.randint(1, 100)

print(rand_number)

print('can you guess the magic number?')
user_in = int(input('What is your guess '))

count = 1
sum = 0
play_again = True

while play_again:
    while rand_number > -100 and play_again:
        count += 1
        sum = sum + count
        if user_in > rand_number:
            print('Lower')
            user_in = int(input('What is your guess '))
            if user_in == rand_number:
                print('you guessed it')
                print(f'you guessed it, it took you {count} atempts')
                break
        elif user_in < rand_number:
            print('higher ')
            user_in = int(input('What is your guess '))
            if user_in == rand_number:
                print(f'you guessed it, it took you {count} atempts')
                break
        elif user_in == rand_number:
            print('You guessed it ')
            break
    
    play_again = input('Do you want to play again, (yes/no)').lower() == 'yes'    

print('thats it ')    
    



# play_again = input('do you want to play again? ').lower() == 'yes'