# Section 22 - Modules
# Modules are nice because I can borrow hundreds (if not thousands) of prewritten modules to work with what I need to work with.
# 1) make HTTP request
# 2) Connect to a database
# 3) Make a web app/game
# What I will learn (Objectives)
# Define what a module is
# Import code from built-in modules
# Import code from other files
# Import code from external modules using pip
# Describe common module patterns
# 'And then we will shift our focus to' Describing the request/response cycle in HTTP
# 'And how we can' Use the requests module to make requests to web apps

# 215 - Working With Built-In Modules
# Why do I care about them?
# Keep Python Files Small. The idea is a lot like using functions. Separate things to make it easier to read what is actually happening.
# Reuse code across multiple files by importing. Likely the best reason to use them
# 'Module' is a fancy way of saying 'another Python file'. I have used them with Scrapy...and in this course for that matter

# built-In Modules
# built-in modules are modules that come with Python by default.
# I still need to import them to use them (since having a bunch of useless stuff in each program would slow things down)
# Think pdb or random, etc.
# A comprehensive list of built-in Python modules: https://docs.python.org/3/py-modindex.html
import random

# randomly picks one
print(random.choice(['apple', 'banana', 'cherry', 'durian']))
# randomly shuffles list
print(random.shuffle(['apple', 'banana', 'cherry', 'durian']))

# if I wanted to refer to the module as another name

# I can now call on the random module using 'rand' instead of 'random'
import random as rand

# randomly picks one
print(rand.choice(['apple', 'banana', 'cherry', 'durian']))
# randomly shuffles list
print(rand.shuffle(['apple', 'banana', 'cherry', 'durian']))

# If I just want to import A PART of a module, I can use keyword 'from'
# It's best to only import what I need to be safe and keep things fast
# from MODULE import * (this imports everything into the current namespace (meaning you dont need random.randint(), just randint()))
from random import choice as c, randint as r

print(c(['a', 'b', 'c', 'd']))
print(r(1, 100))

# 218 - Custom Modules
# Less impressive than it sounds...basically just a file with Python code that I import to another file
# See the lecture for details
# I is the same as importing a built-in module
# just make sure the files are in the same directory (or you need to specify directory location)

# 220 - Installing External Modules and TermColor
# external modules need to be installed and, generally speaking, come from random developers
# A good resource for external modules: https://pypi.org/
# IMPORTANT NOTE: PyPi is not audited. This means I must be extremely careful with the packages I download. Most popular ones will be scrutinized, but others will likely not be...
# to get external packages, I need to use pip in regular Python, but since I'm using Anaconda, I need the cheatsheet:
# https://conda.io/docs/_downloads/conda-cheatsheet.pdf
# It's important to note that I should use different environments as I am testing things out...


# Section 22, Lecture 223 - The Mysterious __name__ variable
# __name__ variable means don't touch
# When run, every Python file has a __name__ variable (whether I declare it or not)
# If the file is the main file being run, its value is '__main__'
# kinda weird to describe here. If I want to learn more, see video 223
# To ignore code on import (VI):
# if __name__ == '__main__':
# this code will not run
# if the file is the main file
