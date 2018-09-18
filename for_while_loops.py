# A for loop basically says, 'for evey character in this thing, do this.

# for item in iterable_object:
# do something with item

# An iterable_object is some kind of collection of items,
# for intance: a list of numbers, a string of characters, a range, etc.

# An item is a new variable that call be called whatever you want
# it is temporary for the for loop...

# item (in the above for loop) references the current position of our iterator within
# the iterable. It will iterate over (run through) every item
# of the collection and then go away when it has visited
# all items.

# for char in 'hello':
# do something
# in this example, char is the item.
# 'hello' is the iterable_object
# char will be 'h' at first, then move on to 'e' and so on
# the do something portion of the program will tell the computer
# to do something if certain conditions are met for each
# character in 'hello' running through each letter until the
# for loop is completed.

# for loops with ranges
# Let's print the number 1-7 using a for loop
for number in range(1, 8):
    print(number)
    # this will square number and print it
    print(number*number)
    # note that because these print functions are in the same loop
    # they 'collate', meaning it prints 1, then 1*1, and so on
    # not 1,2,3,4and then1,2,4,9...

for i in 'coffee':
    print(i)

for i in 'coffee':
    print(i*10)

# WHILE LOOPS
# Anything you can do with a for loop, you can do with a while loop.
# There are a lot of things you can do with a while loop
# that you cannot do with a for loop
# He likes to think of while loops as a distant cousin to
# conditional statements (such as if statement)

# While loops use this format:
# while boolean_value:
    # do something
# While looks will continue to run as long as a condition is truthy.
# eventually it should become falsy (or it will run forever)

user_response = None
while user_response != 'please':
    user_response = input("Say the magic word!")

# while loops require more careful setup than for loops, since
# you need to specify the termination condition manually
# they need a separate variable ahead of time...
# Again, if you do not make the condition false
# at some point, it will run forever and break the program

# this shows how for and while loops can be interchangeable
for num in range(1, 11):
    print(num)
num = 1
while num < 11:
    print(num)
    num += 1
