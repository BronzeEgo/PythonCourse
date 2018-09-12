# In Python, all conditional checks resolve to True or False
#x = 1
# x is 1 IS TRUE
# x=0 IS FALSE

# We can call values that will resolve to True 'truthy', or false 'falsy'.

# Besides False conditional checks, other things that are naturally included: empty objects, empty strings, None, and zero.

# IF I DID THIS:
# if 0:
# print('yay')
# if 1:
# print('yay')
# ONLY THE '1 would print 'yay' since 0 is inherently False

# Some useful code that takes advantage of this principal...

print("What is your favorite animal?")
animal = input()

if animal:
    print(animal + " is my favorite animal too!")
else:
    print("YOU DIDN'T SAY ANYTHING!!!")

# without the 'if' statement above, if the user left the field blank, the return would be ' is my favorite animal too'
# Using the if False dilemma to my advantage creates a situation where the user is forced to input something...
