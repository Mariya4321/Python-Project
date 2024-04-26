import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper and Type 2 for scissors\n"))
game = [rock, paper, scissors]
if choice < 3:
    print(game[choice])
else:
    print("Invalid")
print("Computer Choice: ")
com_choice = random.choice(game)
print(com_choice)
index = game.index(com_choice)
if choice == index:
    print("Draw")
elif (choice == 0) and (index == 1):
    print("You lose")
elif (choice == 1) and (index == 0):
    print("You win")
elif (choice == 2) and (index == 0):
    print("You lose")
elif (choice == 0) and (index == 2):
    print("You win")
elif (choice == 2) and (index == 1):
    print("You win")
elif (choice == 1) and (index == 2):
    print("You lose")
else:
    print("You type invalid number, so you lose!")

