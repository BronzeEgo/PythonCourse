from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
# for time in range(3):
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    print("Best of 5! May the best bot win!")
    print("Type 'q' or 'quit' to quit...")
    player1 = input("Make your move! (Type 'rock', 'paper', or 'scissors'): ").lower()
    if player1 == "quit" or player1 == "q":
        break
    random_num = randint(0, 2)
    if (random_num == 0):
        computer = "rock"
    elif (random_num == 1):
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}")

    if player1 == "rock" and computer == "scissors":
        print("player1 wins!")
        player_wins += 1
    elif player1 == "scissors" and computer == "rock":
        print("computer wins!")
        computer_wins += 1
    elif player1 == "scissors" and computer == "paper":
        print("player1 wins!")
        player_wins += 1
    elif player1 == "paper" and computer == "scissors":
        print("computer wins!")
        computer_wins += 1
    elif player1 == "paper" and computer == "rock":
        print("player1 wins!")
        player_wins += 1
    elif player1 == "rock" and computer == "paper":
        print("computer wins!")
        computer_wins += 1
    elif player1 == "paper" and computer == "paper":
        print("tie")
    elif player1 == "rock" and computer == "rock":
        print("tie")
    elif player1 == "scissors" and computer == "scissors":
        print("tie")
    else:
        print("You do not know how to play the game!")

if player_wins > computer_wins:
    print("You are a winner! WINNING!!!")
elif player_wins == computer_wins:
    print("It's a tie!")
else:
    print("You are a loser! SAD!!!")
print(f"Final Score: Player Score: {player_wins} Computer Score: {computer_wins}")
