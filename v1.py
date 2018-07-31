print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Make your move! (Type 'rock', 'paper', or 'scissors')")
player2 = input("Make your move! (Type 'rock', 'paper', or 'scissors')")

if player1 == "rock" and player2 == "scissors":
    print("player1 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins!")
elif player1 == "paper" and player2 == "paper":
    print("tie")
elif player1 == "rock" and player2 == "rock":
    print("tie")
elif player1 == "scissors" and player2 == "scissors":
    print("tie")
else:
    print("You do not know how to play the game!")
