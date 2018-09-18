# FOR loop:
# basic syntax:
# for item in iterable_object:
#     # do something with item
# list:
# [40, 32, 73]
#
# string:
# "hello"
#
# range:
# range(1,10)
# This would do something with the numbers 1 - 9
#
# range(7) counts stating at 0 and is exclusive. Gives integers 0 - 6
# range (1,8) gives integers 1 - 7 and has two parameters; start and finish
# range( 1, 10, 2) will give you odds from 1 - 10.  The third parameter is called the 'step' meaning how many to step and which way (+-)
# range(7, 0, -1) will give integers from 7 to 1 (counting down)


# this will print 1-7
for number in range(1, 8):
    print(number)


for char in "hello":
    print(char)

# add odd number sbetween 10 and 20
x = 0
for n in range(10, 21):
    if n % 2 != 0:
        x += n
print(x)

# print CLEAN UP YOUR ROOM based on how many times the user wants it printed
times = input("How many times do I have to ask you to clean up your room? ")
times = int(times)
for time in range(times):
    print(f"time {time+1}:CLEAN UP YOUR ROOM!!!!")

# loop through number 1-20 and give each a string
# for x in range(1,21):
#     if x == 1:
#         x = string(x)
#         print(x + " is odd")
#     elif x == 2:
#         print(x + " is even")
#     elif x == 3:
#         print(x + " is odd")
#     elif x == 4:
#         print(x + " is unlucky")
#     elif x == 5:
#         print(x + " is odd")
#     elif x == 6:
#         print(x + " is even")
#     elif x == 7:
#         print(x + " is odd")
#     elif x == 8:
#         print(x + " is even")
#     elif x == 9:
#         print(x + " is odd")
#     elif x == 10:
#         print(x + " is even")
#     elif x == 11:
#         print(x + " is odd")
#     elif x == 12:
#         print(x + " is even")
#     elif x == 13:
#         print(x + " is unlucky")
#     elif x == 14:
#         print(x + " is even")
#     elif x == 15:
#         print(x + " is odd")
#     elif x == 16:
#         print(x + " is even")
#     elif x == 17:
#         print(x + " is odd")
#     elif x == 18:
#         print(x + " is even")
#     elif x == 19:
#         print(x + " is odd")
#     elif x == 20:
#         print(x + " is even")

for num in range(1, 21):
    if num == 4:
        print(f"{num} is unlucky")
    elif num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# OR

for num in range(1, 21):
    if num == 4:
        state = "unlucky"
        # print(f"{num} is unlucky")
    elif num == 13:
        state = "unlucky"
        # print(f"{num} is unlucky")
    elif num % 2 == 0:
        state = "even"
        # print(f"{num} is even")
    else:
        state = "odd"
        # print(f"{num} is odd")
    print(f"{num} is {state}")


# print emojis
# for version
for num in range(1, 11):
    print("\U0001f600" * num)

# while version
times = 1
while times < 11:
    print("\U0001f600" * times)
    times += 1

# while loops
# we can also iterate using while loops, while use this format:
# while im_tired:
#     seek caffiene
#
# while loops will continue to execute while a certain condition is truthy, and will end when it becomes falsy

user_response = None
while user_response != "please":
    user_response = input("Say please bitch!")

# while loops require more careful setup than for loops, since you have to specify the termination conditions manuallyself.
# CAREFUL! If the condition does not become false at some point, your loop will continue forever (or until your computer melts)

msg = input("YOU DO NOT KNOW THE WAY!")
while msg != "I am the Queen":
    print("You are not worthy!")
    msg = input("YOU DO NOT KNOW THE WAY!")
print("PROTECT THE QUEEN!")

for num in range(1, 11):
    print(num)

# this will go on forever
num = 1
while num < 11:
    print(num)

# do this instead
# this worked for him, but is an infinite loop for me...
num = 1
while num < 11:
    num += 1
    print(num + 1)
    # num += 1
