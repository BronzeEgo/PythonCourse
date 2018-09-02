from random import random

#version1
# def flip_coin():
#     #generate a random number from 0 -1
#     r = random()
#     if r > 0.5:
#         #do something
#         return 'Heads'
#     else:
#         #do something else
#         return 'Tails'

# print(flip_coin())


#version2 (I screwed this up...)
def flip_coin():
    #generate a random number from 0 -1
    if random() > 0.5:
        return 'Heads'
    return 'Tails'

print(flip_coin())


