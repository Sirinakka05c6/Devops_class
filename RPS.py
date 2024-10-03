import random

print("Welcome to Rock,Paper or Scissors Game")
print("Let's Start!!!")
rules = input("\nEnter 'y' or 'Y' to display the instructions of the game. ")
if rules=='y' and 'Y':
  print("The user has three choices to pick among 'Rock','Paper' and 'Scissors'.")
  print("If you pick rock and the computer picks scissors, you win. Similarly scissors beat paper, and paper beats rock. ")
else:
  print("\nLet's Start the Game!")

def get_user_choice():
    while True:
        user_choice = input("\nChoose among Rock, Paper, or Scissors: ").strip().capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose either Rock, Paper, or Scissors.")

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "Congratulations! You win the round!"
    else:
        return "Computer wins! Better luck next time :)"

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Your choice is {user_choice}.")
    print(f"The computer choice is {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you wish to continue with the game? (yes/no): ").strip().lower()
    if play_again != "yes":
      print("Thank you for playing! Hope you had fun ^_^")
      break

