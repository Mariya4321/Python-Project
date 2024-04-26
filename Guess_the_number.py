from Guess_no_art import logo
import random

hard_level = 5
easy_level = 10


def random_num():
    random_number = random.randint(1, 100)
    return random_number


def difficulty_lvl():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return easy_level
    elif level == 'hard':
        return hard_level
    else:
        return "Wrong Input"


def guess(turns):
    n = random_num()
    while turns != 0:
        guess_n = int(input("Guess a number: "))
        if guess_n > n:
            if turns == 1:
                print("You've run out of guesses, you lose.")
                turns -= 1
            else:
                print("Too high.")
                print("Guess again!")
                turns -= 1
                print(f"You have {turns} attempts remaining to guess the number.")
        elif guess_n < n:
            if turns == 1:
                print("You've run out of guesses, you lose.")
                turns -= 1
            else:
                print("Too Low.")
                print("Guess again!")
                turns -= 1
                print(f"You have {turns} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {n}.")
            break


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
turns = difficulty_lvl()
print(f"You have {turns} attempts remaining to guess the number.")
guess(turns)
