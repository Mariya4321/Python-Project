from higher_lower import logo, vs, data
import random


def random_data():
    random_a = random.choice(data)
    return random_a


def compare(follow, score_of_game):
    compare_A = random_data()
    compare_B = random_data()
    print(compare_B)
    print(compare_A)


def game():
    print(logo)
    print(vs)
    followers = input("Who has more followers? Type 'A' or 'B': ").lower()
    score = 0
    compare(followers, score)


# random 2 data pick up
# compare
# score
# shifting
game()
