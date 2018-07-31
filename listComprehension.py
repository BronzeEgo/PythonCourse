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

print(doubled_numbers) # same as above output

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
