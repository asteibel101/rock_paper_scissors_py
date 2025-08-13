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

options = [rock, paper, scissors]

def your_valid_choice():
    while True:
        choice = input("Choose 1 for Rock, 2 for Paper or 3 for Scissors. Press Q to exit: ")

        if choice.lower() == "q":
            return None # signal to quit

        if choice.isdigit():
            choice_num = int(choice)
            if 0 <= choice_num  < len(options):
                return choice_num
            else:
                print(f"Number must be between 0 and {len(options) -1}.")
        else:
             print("Invalid input. Enter a number or Q to quit.")


def play():
    player_choice = your_valid_choice()
    computer_choice = random.randint(0, len(options) - 1)

    print(f"You chose {options[player_choice]}")
    print(f"Computer chose {options[computer_choice]}")

    match (player_choice, computer_choice):
        case (p, c) if p == c:
            print("It's a draw!")
        case (0, 2) | (1, 0) | (2, 1):
            print("You win!")
        case _:
            print("Computer wins!")

while True:
    play()

    play_again = input("would you like to play again? Y/N")

    if play_again.lower() != "y":
        print("Goodbye!!!")
        break

    