# This shows how to use for loops
# the user inputs a number and the console spits out
# a string the amount of times the user specifies.

times = input('How many times do I need to tell you? ')
times = int(times)

for time in range(times):
    print(f'time {time + 1}: Clean your room!')
