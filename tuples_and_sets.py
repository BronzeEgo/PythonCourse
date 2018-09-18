# Tuples and Sets.
# Much simpler to discuss than lists and dictionaries.

# Tuple
# An ordered collection or group of items
# tuples are immutable (meaning cannot be changed)(defined forever)
# TUPLES CANNOT BE CHANGED ONCE DEFINED
numbers = (1, 2, 3, 4)

# example of trying to change a tuple
x = (1, 2, 3)
3 in x  # True
# THIS IS COMMENTED OUT BECAUSE IT BREAKS THE CODE!!! x[0] = 'change me' #TypeError: 'tuple' object does not support item assignment

# Why use a tuple?
# 1) Tuples are faster than lists (they run faster because they are more lightweight)
# 2) It makes code safer from bugs becuase tuple is always treated the same
# 3) It is a valid key in a dictionary
# 4) Some methods return them to you - like .items() when working with dictionaries

# commonly unchanged data examples:
# 1) months of the year:
months = ('January', 'February')  # etc

# can be created using () or tuple
# the 'months' variable above is an example of creating one with ()
# below is an example using 'tuple':
# why would I ever do this (except to make it clear to someone what is going on that does not understand what is going on....)
second_tuple = tuple(5, 6, 7)

# accessing tuples (same as lists)
second_tuple[1]  # 6
second_tuple[2]  # 7
second_tuple[-2]  # 7

# Using a tuple as a key in a dictionary
# NOTE: Lists cannot be used as keys in dictionaries, but tuples can
locations = {
    (35, 39.1): 'Tokyo',
    (40, 74.01): 'New York',
    (38, 122.41): 'San Francisco'
}

# .items() returns a tuple (as well as some other undefined dictionary methods)
cat = {"name": "Tink", "Age": "Old"}
# dict_items([('name', 'Tink'), ('Age', 'Old')]) #Those are tuples in there...
cat.items()

# Tuple looping and methods
# Looping over tuples uses same syntax as looping over lists
names = ('Kris', 'john', 'matt', 'cole')

for name in names:
    print(name)

i = len(names) - 1
while i >= 0:
    print(names[i])  # print out names in reverse
    i -= 1  # increment by -1

# 2 methods for tuples
# count
# return the number of times a value is in a tuple
x = (1, 2, 3, 3, 3)
x.count(3)  # 3
x.count(2)  # 1

# index
# returns the index at which a value is found in a tuple
x.index(1)  # 0
x.index('r')  # ValueError
x.index(3)  # Even though three is in there 3 times, it will only show '2' as the index

# I can have nested tuples
numb = (1, 2, 3, (4, 5), 6, 7)  # There is a tuple in a tuple

# slices and nested lists work the same as with a list (see lists.py)


# Sets
# Sets and tuples don't have much to do with one another.
# They are not commonly used together
# They are both collections of data and are lighterweight than a list or dictionary
# Sets are like formal mathematical sets
# Sets do not have duplicate values
# Elements in sets are not ordered
# Items in a set cannot be accessed by index
# Sets can be useful to keep track of a collection of elements, but don't care about the orderm keys or values and duplicates (very restrictive)

# sets cannot have duplicates
s = set({1, 2, 3, 4, 5, 5, 5})  # {1,2,3,4,5}

# How to create a set
s = set({1, 4, 5})

# Creating a set with the same values as above (you don't need the word 'set')
s = ({1, 4, 5})

4 in s  # True
8 in s  # False

# for loop with set
for thing in s:
    print(thing)

# common usecase for set
# the list has duplicates and you don't want them
cities = ['LA', 'Philly', 'NY', 'DC', 'NY']
print(list(set(cities)))
# if I wanted to know how many unique cities there are in above list:
print(len(set(cities)))

# set methods and set math
# working with sets is very common, there are a lot of things that can be done
# add
# add adds a piece of data to a set
s = set([1, 2, 3])
s.add(4)  # {1,2,3,4}
s.add(4)  # {1,2,3,4}...the second 4 is not added since sets request unique values

# remove
# remove removes a value from a set
s.remove(4)  # {1,2,3}
# an error will be thrown if you try to remove something that is not there
# using .discard() will try to remove items and, if the item didn't exist before running the code, an error is not thrown

# copy
# copy copies set (same as in lists.py)

# clear
# clear removes all values in a set (see lists.py)

# set math
# will find intersection, union, or symmetric_difference, etc.
# see video 142 around 5:25

# set comprehension
{x**2 for x in range(10)}  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
# VS (to get a dictionary)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
{x: x**2 for x in range(10)}

# function set comprehension


def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5
