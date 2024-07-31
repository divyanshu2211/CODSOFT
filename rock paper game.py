import random

def get_user_choice():
    """
    Function to get user's choice for Rock-Paper-Scissors.
    """
    user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    return user_choice

def get_computer_choice():
    """
    Function to get computer's random choice for Rock-Paper-Scissors.
    """
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """
    Function to determine the winner of the game.
    """
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    """
    Function to play Rock-Paper-Scissors game.
    """
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        determine_winner(user_choice, computer_choice)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
