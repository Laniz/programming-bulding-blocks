secret_word = "shepherd"  
num_guesses = 0  

while True:
    guess = input("What is your guess: ")  
    num_guesses += 1  
    
    if guess == secret_word:
        print(' ')
        print("Congratulations! You guessed it!")
        print("Number of guesses: ", num_guesses)
        break  
    
    else:
        print(' ')
        print("Your guess was not correct.")
        
print("It took you", num_guesses, "attempts to guess the secret word.")
