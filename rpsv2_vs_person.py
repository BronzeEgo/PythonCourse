# I am altering this more. I'm going to add a class for PvP and PvE (player vs computer)
# I've never done this before, but I think I can since I have in other languages...
# ...Beyond the scope of what I've learned so far. The 'class PVP' works if I remove the
# class, tab it all in, and comment out everything that has to do with picking the game mode...
#print("Welcome to")
# print("Rock...")
# print("Paper...")
# print("Scissors...")
# print("")
#print("Would you like to pay against a computer or person?")
# print("")
#print("Type 'person' to play with a friend")
#print("Or type 'computer' to play against the computer")
#game_mode = input()

# if game_mode = 'person':


# This produces the same results as 'rpsv2.py' but is a bit more streamlined...
# class PvP
print("Rock...")
print("Paper...")
print("Scissors...")
print("AGAINST A PERSON!!!")

# I added this in so the players could name themselves
# In his, players were always labeled as 'Player1' or 'Player2'
player1name = input("Player1, what is your name? ")
player2name = input("Player2, what is your name? ")

player1 = input(player1name + ", make your move: ")
player2 = input(player2name + ", make your move: ")

if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print(player1name + " wins!")
    elif player2 == 'paper':
        print(player2name + " wins!")
elif player1 == "paper":
    if player2 == "rock":
        print(player1name + " wins!")
    elif player2 == 'scissors':
        print(player2name + " wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print(player1name + " wins!")
    elif player2 == 'rock':
        print(player2name + " wins!")
else:
    print("Something went wrong...Make sure you spell 'rock', 'paper', and 'scissors' exactly like this (CAPITALIZATION MATTERS)")

# class PvE
    # print("Rock...")
    # print("Paper...")
    # print("Scissors...")
    #print("AGAINST A PERSON!!!")
