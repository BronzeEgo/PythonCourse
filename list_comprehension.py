# List Comprehension
# 'One of th emost powerful and unique features to python
#'The idea of comprehension applies to many other data structures that we will learn about later'
# 'Things like dictionaries and sets, tuples, generators, all laters
# understanding them is critical

# What does it do?
# Shorthand syntax that allows me to make new lists or generate copies of current lists, or, more often than not, tweaked versions of lists
# example: take a list and generate a new one that has every number squared

# the syntax
# [__for__in__]
# the first two variable names in the furmula are always the same
# 'in' another list or range or something that can be iterated through...

nums = [1, 2, 3]

times_10 = [x*10 for x in nums]  # [10, 20, 30]
print(times_10)

divide_2 = [x/2 for x in nums]  # [0.5, 1.0, 1.5]
print(divide_2)

# This could be done in a loop, but is easier with list comprehension
# Example using the above num in a loop instead

nums = [1, 2, 3]
doubled_nums = []

for num in nums:
    doubled_num = num * 10
    doubled_nums.append(doubled_num)

print(doubled_nums)
# Obviously a lot more code than 'nums = [1,2,3]/n[x*10 for x in nums]/nprint(times_10)'

# another list comprehension example:
name = 'kris'
upper_name = [char.upper() for char in name]  # ['K', 'R', 'I', 'S']
print(upper_name)

# another example(may be useful to capitalize first letter of stuff):
friends = ['ashley', 'matt', 'mike']
proper_friends = [friend[0].upper() + friend[1:] for friend in friends]

print(proper_friends)

# example using a range:
new_nums = [num*10 for num in range(1, 6)]  # [10, 20, 30, 40, 50]
print(new_nums)

# example using boolean:
bool_example = [bool(val) for val in [0, [], '']]
print(bool_example)  # [False, False, False]

# example converting a list of numbers to a list of strings:
numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list)  # ['1', '2', '3', '4', '5']

# Adding conditional logic to list comprehension
# such as if and else

# This example will create two new lists from the first
# one being even numbers, the other odd
nums = [1, 2, 3, 4, 5, 6]

# Use a modulus to find even #[2, 4, 6]
evens = [num for num in nums if num % 2 == 0]
# use modulus to find odds #[1, 3, 5]
odds = [num for num in nums if num % 2 != 0]
print(evens)
print(odds)

# using else conditional logic example:
else_example = [num*2 if num % 2 == 0 else num/2 for num in nums]
print(else_example)  # [0.5, 4, 1.5, 8, 2.5, 12]

# This is a weird one, but it will remove vowels (example of not in):
with_vowels = "This is so much fun!"

without_vowels = ''.join(char for char in with_vowels if char not in 'aeiou')
print(without_vowels)  # 'Ths s s mch fn!'

# nested list comprehension:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# prints 1 - 9 taken from nested_list on separate lines
[[print(val) for val in i] for i in nested_list]

# another example of nested list comprehension:
board = [[num for num in range(1, 4)] for val in range(1, 4)]

print(board)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

new_board = [['X' if num %
              2 != 0 else 'O' for num in range(1, 4)] for val in range(1, 4)]

# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']] #The first part is repeated 3 times
print(new_board)


# OLD STUFF
# the syntax
# __ for __ in __

# nums = [1, 2, 3]
#
# [x*10 for x in nums]

# Take a list and change it, creating a new list

# Not list comprehension
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = []
#
# for num in numbers:
#     doubled_numbers = num * 2
#     doubled_numbers.append(doubled_numbers)
#
# print(doubled_numbers) # [2, 4, 6, 8, 10]

# OR

# list comprehension
numbers = [1, 2, 3, 4, 5]

doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)  # same as above output

# ------------------------------

# [value for value in variable] (you get this by typing 'lc')

# lc with COnditional Logic
numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]

odds = [num for num in numbers if num % 2 != 0]

# The if must come after the lc Logic

# Same as above, just condensed
[num*2 if num % 2 == 0 else num/2 for num in numbers]
# [0.5, 4, 1.5, 8, 2.5, 12]

with_vowels = 'This is so much fun!'

''.join(char for char in with_vowels if char not in "aeiou")
print(with_vowels)
# "Ths s s mch fn!"
