#define the word
word = "shepherd"
secret_word = "_" * len(word)

#set the number of guesses to 0 and limit the number of tries
guesses = 0
tries = 0
max_tries = 7

#start the loop with A while true
while True:
    # print(secret_word)
    guesses += 1
    tries += 1
    print('You have 8 tries, one for each letter.\n ')
    print(secret_word)
    guess = input(f"Enter a guess ({len(word)} letters): ").lower()

    #when the word is guessed first try
    if guess == word:
        print("Congratulations, you won!")
        break

    #if letters are not equal to the word
    if len(guess) != len(word):
        print(f"Your word must have {len(word)} letters.")

    if tries > max_tries:
        print("Sorry, you lost! The word was:", word)
        break    

    #if not above conditions go to the main loop    
    else:
        # guesses += 1
        new_hidden_word = ""
        for i in range(len(word)):
            if guess[i] == word[i]:
                new_hidden_word += guess[i].upper()
            elif secret_word[i] != "_":
                new_hidden_word += secret_word[i]
            elif guess[i] in word:
                new_hidden_word += guess[i].lower()
            else:
                new_hidden_word += "_"
        secret_word = new_hidden_word

print(f"You made {guesses} guesses.")
