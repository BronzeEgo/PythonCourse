import random


num = random.randint(1,10)
user = None

while user != num:
    user = int(input("What is your guess between 1 and 10? "))
    if num > user:
        print("Too low! Guess again.")
    elif num < user:
        print("Too high! Guess again!")
    elif num == user:
        print("Correct! Well done.")
