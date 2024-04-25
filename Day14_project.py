from higher_lower import logo, vs, data
import random


def data_format(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, {account_country}"


def random_data():
    return random.choice(data)


def compare(guess, follow_a, follow_b):
    if follow_a > follow_b:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    compare_B = random_data()
    is_continue = True
    while is_continue:
        compare_A = compare_B
        compare_B = random_data()
        while compare_A == compare_B:
            compare_B = random_data()

        print(f"Compare A: {data_format(compare_A)}")
        print(vs)
        print(f"Against B: {data_format(compare_B)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        followersA = compare_A["follower_count"]
        followersB = compare_B["follower_count"]

        is_correct = compare(guess, followersA, followersB)

        if is_correct:
            score += 1
            print(logo)
            print(f"You're right!, current score is {score}.")
        else:
            print(f"Sorry, that's wrong!, Final score is {score}.")
            is_continue = False


# random 2 data pick up
# compare
# score
# shifting
game()
