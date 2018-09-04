#smaller an more concise than functions part 1
#focused on just a few new topics
#Objectives:
#use the * and ** as parameters to a function and outside a functions
#Leverage dictionary and tuple uppacking to create more flexible functions

#*args (single star arguments)
#a special operator I can pass to functions
#It gathers remaining arguments as a tuple
#This is just a parameter - I can call it whenever I want
#example:
#the old way
def sum_all_nums(num1, num2, num3):
    return num1+num2+num3
print(sum_all_nums(4,16,9))
#the new way:
#This will allow you to pass any amount of arguments through sum_all_nums with a basic single parameter
def sum_all_nums_args(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums_args(2,4,5,6,7))

#to all other parameters to args:
#note that 'num1' is not included in args argument and output
def sum_all_nums_args1(num1, *args):
    print(num1)
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums_args1(2,4,5,6,7))

#another example:
def ensure_correct_info(*args):
    if 'Colt' in args and 'Steele' in args:
        return 'Welcome back Colt!'
    return 'Not sure who you are...'

print(ensure_correct_info('rekt', "I'm here to HACk you normie", 'Bitch')) #not sure who you are
print(ensure_correct_info(1, True, 'Steele', 'Colt')) #Welcome back Colt!

#note that the '*' needs to be first, but otherwise, you can call the parameter whatever you want.
#note note 'args' is the convention for this type of code.

#**kwargs
#different from *args
#a special operator I can pass to function
#Rather than gathering just any additional argument, it will gather remaining keyword arguments as a dictionary
#Like *args, it is just another parameter, you can call it whatever you like (as long as it starts with **)

#an example:
#the old way:
# def fav_colors(colt='purple', ruby='red',ethel='teal'):
#     for i in fav_colors.value():
#         print(i)
# fav_colors(colt='purple', ruby='red',ethel='teal')

#the new way:
def fav_colors(**kwargs):
    for person,color in kwargs.items():
        print(f"{person.title()}'s favorite color is {color}.")

fav_colors(colt='purple', ruby='red',ethel='teal')

#another_example:
def special_greeting(**kwargs):
    if 'David' in kwargs and kwargs['David'] == 'special':
        return 'You get a special greeting David!'
    elif 'David' in kwargs:
        return f"{kwargs['David']} David!"
    return 'Not sure who this is...'

print(special_greeting(David='Hello')) #Hello David!
print(special_greeting(Bob='hello')) #Not sure who this is...
print(special_greeting(David='special')) #You get a special greeting David!

#ordering parameters
#I'm guessing the *args or **kwargs has to come last, and the rest must be in order at the beginning, unless you use a keyword argument when making an argument against a parameter
#kinda what I thought
#1) parameters (a,b)
#2) *args (*args)
#3) default parameters (instructor='Colt')
#4)kwargs (**kwargs)

#VI for real data manipulation!!!
#tuple unpacking
#* can be used as an argument as well as a parameter
#this will allow you to unpack values


#example:
def sum_all_nums_args12(*args):
    total = 0
    for num in args:
        total += num
    print(total)
    return total
#This will work with both tuples and lists
nums1 = [1,2,3,4,5,6]
print(sum_all_nums_args12(*nums1))

#dictionary unpacking
#probably use ** instead of * in argument
#see lecture 182 for more
def display_names(first, second):
    print(f"{first} says hello to {second}")
names = {'first': 'colt', 'second': 'rusty'}

display_names(**names)

#a simple calulator using everything I've learned so far:
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final