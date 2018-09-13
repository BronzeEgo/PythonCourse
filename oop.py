# object oriented programming

# 232 - Intro
# objectives:
# 1) Define what OOP is
# 2) Understand encapsulation and abstraction
# 3) create classes and instances and attach methods and properties to each

# 233 - Defining Classes and Objects
# What is OOP?
# Basically, it is using code to represent something in the real world (car, mouse, cat)
# This is done using classes and objects
# Class
# A class is a blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict).
# instance(object)
# instances(object) are objects that are constructed from a class bluerpint that contain their class's methods and properties.
# all the built in methods I have been using are classes (int, list, float, etc.)
# when I do num = [1,2,3] I am creating an instance of the class list with the name nums
# note: when I create my own classes, they will be called in a different way from the built in ones (such as card = Card('Jack', 'Diamonds'))

# 234 - Abstraction and Encapsulation
# Why OOP?
# With OOP, the goal is to encapsulate your code into logical, hierarchical groups using classes so that you can reason about your code at the higher level
# example
# Say I want to make a poker game
# I could have the following entities:
# - game
# - player
# - card
# - deck
# - hand
# - chip
# - bet
# - probably more

# encapsulation
# encapsulation is the grouping of public and private attributes and methods in a programmatic class, making abstraction possible
# example:
# When designing a deck class, I make cards a private attribute (a list) (I will never directly access .cards())
# I decide that the length of the cards should be accessed via a public method called count() -- i.e. Deck.count()

# abstraction
# abstraction is exposing only the 'relevant' data in a class interface, hiding private attributes and methods (aka the 'inner workings') from users

# 235 - Creating Classes and Instances
# Some notes about classes:
# Always name them in the singular (user vs users)
# Name them using camelcase


class Person:
    # the work 'pass' allows me to say 'I'm done, move on'. This avoids breaking the code.
    pass


p = Person()
print(type(p))
