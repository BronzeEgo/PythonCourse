#syntax
#regular function:
def square(num):
    return num * num
print(square(9))
#now a lambda that does same thing:
lambda num: num * num
#as variable
square2 = lambda num: num * num
print(square(9))

#lambdas are basically functions with no name
#some people call them anonymous functions
