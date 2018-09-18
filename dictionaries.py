# Dictionaries
# another data structure

# Lists vs Dictionaries
# Limitations of Lists
# Good for a particular type or set of data...
# Users, names, items, make a good list

# something not good for a list:
instructor = ['Colt', True, 4, 'Python', False]
# The above data doesn't really mena much without context...
# This is where a dictionary comes in.

# a dictionary is a data structure that consists of key value pairs.
# keys are used to describe the data and the values to represent the data

# a dictionary:
instructor = {
    'name': 'Colt',
    'owns_dog': True,
    'num_courses': 4,
    'favorite_language': 'Python',
    'is_hilarious': False,
    44: 'his favorite number'
}

# making the above list into a list dictionary:
instructor2 = [{'name': 'Colt', 'owns_dog': True, 'num_courses': 4, 'favorite_language': 'Python', 'is_hilarious': False},
               {'name': 'Mark', 'owns_dog': True, 'num_courses': 6, 'favorite_language': 'Java', 'is_hilarious': True}]
# I could then make infinite dictionaries in the list to represent, lets say, vape products...

# a note on dictionaries vs JSON:
#'JSON is a data format (a string), Python dictionary is a data structure (in-memory object).'
# 'If you need to exchange data between different (perhaps even non-Python) processes then
#' you could use JSON format to serialize your Python dictionary.'
# additional reading at https://www.reddit.com/r/learnprogramming/comments/4va31v/what_is_the_difference_between_a_python/

# another way to make a dictionary is to use the 'dict' function:
# NOTE, the key cannot be a string in this style, but is converted to a string?
another_dictionary = dict(clay='value')
another_dictionary  # {'clay': 'value'}

another_dictionary2 = dict(clay='value', clay2='T', clay3=3)  # etc
another_dictionary2  # {'clay': 'value', 'clay2': 'T', 'clay3': 3}

# accessing individual values in a dictionary
another_dictionary2['key']  # 'value'
another_dictionary2['key3']  # 'value3'

# iterating dictionaries
# how to get all of them (what some number)(iteration)
instructor = {
    'name': 'Colt',
    'owns_dog': True,
    'num_courses': 4,
    'favorite_language': 'Python',
    'is_hilarious': False,
    44: 'his favorite number'
}

# looping for keys
for key in instructor.keys():
    print(key)  # this will print keys for 'intructor' on their own lines

# looping for values
for value in instructor.values():
    print(value)  # this will print values for 'intructor' on their own lines

# looping for both keys and values at same time
# note that there are 2 things being iterated over in 'instructor'
for key, value in instructor.items():
    print(str(key) + ':', str(value))

# testing for existence of key or value in dictionary
# Using In With Dictionaries

# testing for keys
'name' in instructor  # True
'awesome' in instructor  # False
if 'phone' in instructor:
    print('There is a phone key')
else:
    print('There is no phone key')

# testing for values
'Colt' in instructor.values()  # True
'awesome' in instructor.values()  # False
if 'phone' in instructor.values():
    print('There is a phone key')
else:
    print('There is no phone key')

# testing for both keys and values
4 in [x for t in instructor.items() for x in t]
# OR
4 in instructor.keys() or 4 in instructor.values()

# Dictionary Methods
# Clear
# Clear will empty the dictionary
d = dict(a=1, b=2, c=3)
d.clear()
d  # will return an empty dictionary

# Copy
# Copy will make a copy of a dictionary
d = dict(a=1, b=2, c=3)
c = d.copy()
c  # will ouput the same thing as d would
c is d  # I've created a new dicitonary that is stored elsewhere.

# fromkeys
# fromkeys works different from other methods
# it creates key-value pairs from comma separated values
{}.fromkeys('a', 'b')  # created {'a': 'b'}
# This is merging a list and a string to make {'emails': 'unknown'}. If there were multiple items in the key list, it would assign each the vlaue 'unknown'
{}.fromkeys(['emails'], 'unknown')
# This is showing what I was talking about at the end of the previous comment. {'emails': 'unknown', 'phone': 'unknown'}
{}.fromkeys(['emails', 'phone'], 'unknown')
# This add a single key to the list making {'a': [1,2,3,4,5]}
{}.fromkeys('a', [1, 2, 3, 4, 5])

# a good use for this
new_user = {}.fromkeys(['name', 'score', 'email', 'bio'], 'unknown')

# get
# get will get a value. IMPORTANTLY, it will return None instead of KeyError if the key does not exist
# very useful for dictionaries (or list) containing vape details that are incomplete. Otherwise, an error will be thrown and the program will stop everytime a value is missing
d = dict(a=1, b=2, c=3)
d['a']  # 1
d.get('a')
d['b']  # 2
d.get('b')  # 2
d['no_key']  # KeyError
d.get('no_key')  # None

# pop
# pop takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed
d = dict(a=1, b=2, c=3)
d.pop('a')  # removes and returns '1'
d.pop('f')  # KeyError
d.popitem()  # removes something random

# update
# update will update keys and values in a dictionary with another set of key value pairs
# similar to copy, but if you wanted to update an existing list with the values of another.
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}
second.update(first)
second  # this will show second has the same values as first
second['a'] = 'AMAZING'  # making 'a' 'AMAZING'
second.update(first)
second  # The update will show that second has been reverted to the values of 'first'


# dictionary comprehension
# similar to list comprehension, but different
# the syntax:
# {___:___for___in___}
# dictionary conprehension iterates over keys by default
# If I want to iterate over keys and values, I need to use .items()

# first example
numbers = dict(first=1, second=2, third=3)
# note that ** squares the value
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)  # {'first': 1, 'second': 4, 'third': 9}

# another example
nums = {num: num**2 for num in [1, 2, 3, 4, 5]}
print(nums)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# another example
# This makes str1 the keys and str2 the values in a new dictionary called combo
str1 = 'ABC'
str2 = '123'
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)  # {'A': '1', 'B': '2', 'C': '3'}

# another example
# This one capitalizes everything is a dictionary
instructor = {'name': 'colt', 'city': 'san francisco', 'color': 'purple'}
yelling_instructor = {k.upper(): v.upper() for k, v in instructor.items()}
# {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}
print(yelling_instructor)
# Same as above, but see output
instructor = {'name': 'colt', 'city': 'san francisco', 'color': 'purple'}
yelling_instructor = {k.upper() if k is 'color' else k: v.upper()
                      for k, v in instructor.items()}
# {'name': 'COLT', 'city': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}
print(yelling_instructor)

# conditional logic with dictionary comprehension
num_list = [1, 2, 3, 4]
var = {num: ('even' if num % 2 == 0 else 'odd') for num in num_list}
print(var)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
# same thing as above with a range
num_list = [1, 2, 3, 4]
var = {num: ('even' if num % 2 == 0 else 'odd') for num in range(1, 100)}
print(var)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'...through 100}

# This one was the answer to an exercise, but wanted to add it here
# Python will output an ASCII character if you give it the right combination of character
# This may be useful for things such as adding html or css to a url without changing the url
# such as I did in VBA for Apps
answer = {count: chr(count) for count in range(65, 91)
          }  # run this to see what you get
# the output is not that important, other than the fact that it is cleaver, but the chr65 ('A') may be very useful...
