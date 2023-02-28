import random

# Define the list of words
words = ["shepherd", "computer", "mountain"]

# Set the maximum number of guesses
max_guesses = 6

# Loop through each word in the list
while True:
    # Randomly select a new word from the list
    word = random.choice(words)
    secret_word = "_" * len(word)
    guesses = 0

    # Start the loop with while True
    while True:
        print(secret_word)
        guesses += 1
        guess = input(f"Enter a guess ({len(word)} letters): ").lower()

        # Check if the guess is a valid input
        if not guess.isalpha():
            print("Please enter only letters.")
            continue

        # When the word is guessed correctly
        if guess == word:
            print("Congratulations, you won!")
            break

        # When the guess is incorrect
        if len(guess) != len(word):
            print(f"Your guess must have {len(word)} letters.")
        else:
            new_hidden_word = ""
            for i in range(len(word)):
                if guess[i] == word[i]:
                    new_hidden_word += guess[i].upper()
                elif secret_word[i] != "_":
                    new_hidden_word += secret_word[i]
                else:
                    new_hidden_word += "_"
            secret_word = new_hidden_word

        # Check if the maximum number of guesses has been reached
        if guesses >= max_guesses:
            print("Sorry, you lost! The word was:", word)
            break

    print(f"You made {guesses} guesses for the word '{word}'.\n")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again != 'y':
        break
