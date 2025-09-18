import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    print("Let's play Rock, Paper, Scissors!")
    
    while True:
        computer = random.choice(choices)
        player = input("\nEnter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        
        if player == 'q':
            print("Thanks for playing!")
            break
            
        if player not in choices:
            print("Invalid choice! Please try again.")
            continue
            
        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")
        
        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win! 🎉")
        else:
            print("Computer wins! 😅")

play_game()