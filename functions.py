# Functions

# Function structure


def name_of_function():
    # block of code
    print("Hi!")


# defining a function will not run (execute code)
# to call it, do this:
name_of_function()

# Returning values from functions
# What does it mean to return values?
# return exits the function
# outputs whatever value is placed after the return keyword
# pops the function off the call stack (basically removes the function from the tasks that Python needs to complete)


def hi():
    return 'hi'
    # This does not show any output because return exited the function before it could be run.
    print('This will not show')


def square_of_7():
    7**2
    'alkjha'


    # the above code will not return a value out, so, if I did this:
results = square_of_7()
print(results)  # None
# VSCode was nice wnough to tell me that this was bad
# the code will still run, but I get 'None' instead of '49'

# If I want the above to return something, I would need to write it like this:


def square_of_7_():  # I cannot have 2 functions with same name
    return 7**2
    # VSCode is nice enough to let me know this is 'unreachable' because it does nothing...
    'alkjha'


    # the above code will not return a value out, so, if I did this:
results2 = square_of_7_()
print(results)  # None

# function parameters


def square(num):
    return num*num


print('What number would you like squared?')
user = int(input())
print(square(user))

# adding in a function
# multiplication is done in the same way, except use a '*' instead of '+'


def add(a, b):
    return a+b

# naming parameters


def print_full_name(string1, string2):
    return(f'Your full name is {string1} {string2}')

# there is a difference between a parameter and argument
# many peopleuse them interchangably, BUT THEY ARE WRONG (remember the octothorp)
# a parameter is a variable in a function definition
# def print_full_name(string1, string2): #between the () is a set of parameters
# When you call a function or method, the arguments are the data you pass into the method's parameters
# parameter is variable in the declaration of the function
# the argument is the actual value of this variable that gets passed to functions
# he makes it really clear around 7:30, video 152, section 17
# order of parameters and arguments are important

# common mistakes when returning
# this looks like it will work, but instead of 16, it gives 1
# indentation is very important
# the return is in wrong spot


def sum_odd_numbers_wrong(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total


print(sum_odd_numbers_wrong([1, 2, 3, 4, 5, 6, 7]))  # 1

# This is the above code with correct indentations:


def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))  # 16

# this is a arbitrary issue. Won't break code, but wil make it nicer:


def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:
        return False


print(is_odd_number(4))  # False
print(is_odd_number(9))  # True

# The more concise version of the above code:


def is_odd_number_concise(num):
    if num % 2 != 0:
        return True
    return False


print(is_odd_number(4))  # False
print(is_odd_number(9))  # True

# functions default parameters


def exponents(num, power):
    return num ** power


print(exponents(2, 3))  # 8

# now lets say we want the above function to default to squaring (**2) if a second parameter is not given


# th2 '=something' after the parameter gives it a default value
def exponents_default_square(num, power=2):
    return num ** power


print(exponents_default_square(2, 3))  # 8
print(exponents_default_square(4))  # 16

# why have default parameters?
# 1) Allows you to be more defensive
# 2) Avoids errors with incorrect parameters
# 3) More readable examples

# What can default parameters be?
# Basically anything
#functions, lists, dictionaries, strings, booleans
# an example of a function as a parameter:


def adds(a, b):
    return a+b


def math(a, b, fn=adds):
    return fn(a, b)


def subtract(a, b):
    return a-b


# This stuff doesn't work because if the user inputs '2,3' then python thinks I am not using a base 10 system
# I'd have to break the input into 2 variuables somehow.
# I will keep going for now with the knowledge that it is broken and VSCode didn't catch it...
print('You can add or subtract 2 numbers')
print('The first value will be subracted from the second and vice versa')
print('If you want to add, you do not need a third argument')
print('example: 2,3 and then return key will give result "5"')
print('example: 2,3, subtract and then return key will give result "-1"')
use = int(input())
print(math(use, use, use))

# keyword arguments
# example:


def full_name(first, last):
    return 'Your name is {first} {last}'


# Using keyword arguments, I can input things out of order:
full_name(first='Colt', last='Steele')
# note how I was able to provide the arguments out of order by providing the parameter as a keyword
full_name(last='Steele', first='Colt')

# Why use a keyword argument?
# It is not very useful when there are just a couple parameters to mess with, but if using something such as a dictionary with countless entries
# you don't need to remember the index of the parameter to make a change to it
# I guess it makes thinks more 'human friendly' one the variable count gets out of hand.

# Scope
# Where our variables can be accessed
# I already have a good indea of this...
# Is the class global or local to the operation...
# As I said, variables defined within a function are 'scoped' to that function.
# they are not callable outside it

# if I want to call the global variable rather than the local one, I use the 'global' keyword
total = 0


def increment():
    global total
    total += 1
    return total


print(increment())

# still in regards to scope, nonlocal
# nonlocal lets me modify a parent's variables in a child (aka nested) function


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner

# how to document functions
# use """ """
# very useful to expain complex functions


def say_hello():
    """A simple function that returns the string hello"""
    return 'Hello'


say_hello.__doc__  # outputs 'A simple function that returns the string hello'

# built in functions have documentation as well
print.__doc__
# outputs:
# "print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:
# a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value,
# default a newline.\nflush: whether to forcibly flush the stream."

# Returns
# This was not in the lectures, but it tripped me up enough that I wanted to put it here.
# Some things, like len('hello') naturally return a value, in this case 5
# Others, like comment.insert(3, value) do not return anything besides None.
# To get values out of that, I need to return the thing being updated before the function is finished (the return will finish it) if I want the value
#comment.insert(3, value)
# return comment
# By doing this, I get the updated 'comment' item instead of None
# I will need to be careful with this in the future since I will likely be doing a lot of data manipulation in this way.
