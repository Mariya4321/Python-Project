import random

from hangman_words import word_list

from hangman_art import logo

random_word = random.choice(word_list)
lives = 6

print(logo)  # Logo of Hangman

hidden_word = []  # null list
for _ in range(len(random_word)):
    hidden_word += '_'  # Filling list with '_'
print(hidden_word)
end = False
while not end:  # When end variable will be True
    guess = input("Enter any letter : ").lower()
    ch = 0

    if guess in hidden_word:  # Checking letter in random selected word
        print(f"You've already guessed {guess}")  # when already guessed
    for i in random_word:  # selecting each letter of word
        if guess == i:  # comparing the guess from selected letter
            hidden_word[ch] = i     # Replacing '_' from letter
        ch += 1
    if guess not in hidden_word:    # If guess is wrong
        lives -= 1      # losing lives
        if lives == 0:
            end = True  # escaping/breaking while loop
            print("You lose")
            print(f"The Word was {random_word}")        # Final word selected randomly
    print(f"{' '.join(hidden_word)}")       # changing list to string
    if '_' not in hidden_word:      # checking empty spaces
        end = True
        print("You win")

    from hangman_art import stages

    print(stages[lives])    # lives remaining
# while loop ends
