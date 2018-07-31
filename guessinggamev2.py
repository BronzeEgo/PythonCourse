import random


num = random.randint(1,10)
user = None

while True:
    user = int(input("What is your guess between 1 and 10? "))
    if num > user:
        print("Too low! Guess again.")
    elif num < user:
        print("Too high! Guess again!")
    elif num == user:
        print("Correct! Well done.")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            num = random.randint(1,10)
            user = None
        else:
            print("Thanks for playing!")
            break
