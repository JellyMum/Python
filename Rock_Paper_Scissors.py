import random

# create a list of options
options = ["rock", "paper", "scissors"]

# set the initial score to 0
player_score = 0
computer_score = 0

# ask the player if they want to play
play_again = True
while play_again:
    # ask the player to choose an option
    player_choice = input("Choose Rock, Paper, or Scissors: ").lower()

    # randomly select an option for the computer
    computer_choice = random.choice(options)

    # print the choices
    print("You chose:", player_choice)
    print("The computer chose:", computer_choice)

    # determine the winner and update the score
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors" or \
         player_choice == "paper" and computer_choice == "rock" or \
         player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        player_score += 1
    else:
        print("The computer wins!")
        computer_score += 1

    # print the score
    print("Score:")
    print("Player:", player_score)
    print("Computer:", computer_score)

    # ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n)").lower() == "y"
