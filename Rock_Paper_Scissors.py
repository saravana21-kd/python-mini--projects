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

games = [rock, paper, scissors]

user_choice = int(
    input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors:\n> ")
)

if user_choice < 0 or user_choice > 2:
    print("Invalid choice. You lose.")
else:
    print("\nYou chose:")
    print(games[user_choice])

    computer_choice = random.randint(0, 2)
    print("\nComputer chose:")
    print(games[computer_choice])

    if user_choice == computer_choice:
        print("Match Draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("Computer wins!")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("Computer wins!")
