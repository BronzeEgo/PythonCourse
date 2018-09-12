# This allows a user to guess a number between 1 and 10
# Note that randint is inclusive (meaning 1,10 is actually 1 - 10)

import random


num = random.randint(1, 10)
user = None

while user != num:
    user = int(input("What is your guess between 1 and 10? "))
    if num > user:
        print("Too low! Guess again.")
    elif num < user:
        print("Too high! Guess again!")
    elif num == user:
        print("Correct! Well done.")
        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again == 'y':
            num = random.randint(1, 10)
        else:
            print('thank you for playing')
            break


print(f'The number was {num}.')
