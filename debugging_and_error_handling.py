#section 21
#I have a feeling I will not take many notes here
#when I do run into errors, google will be a great resource
#and I already have an idea of how they work (when I'm thrown a decently explicit error)

#207 intro
#I will be taking some notes and examples down
#pdb to set breakpoints and step through code to find errors
#try and except blocks to handle the errors. this will allow the application to finish even if I get an error (which I will)

#208 - Common Types of Errors
#syntax
#name
#type
#index
#value
#key
#attribute
#many more not in this video

#209 - Raising Your Own Errors
#This is how I can say something specific that is going wrong in code I have written
raise ValueError('invalid value') #This would print value error and tell the recipient 'invalid value'

def colorize(t, c):
    colors = ('cyan', 'yellow', 'blue')
    if type(c) is not str:
        raise TypeError('color must be a string')
    if type(t) is not str:
        raise TypeError('text must be a string')
    if c not in colors:
        raise ValueError('color must be cyan, yellow, or blue')
    print(f"Printed {t} in {c}")

colorize(4, 4)
#This will be very useful in the future to let me know that something is wrong that is outside the scope of what Python believes to be right or wrong

#210 - Try and Except Blocks (Handle Errors!)
#This will show how to handle errors and move on from them
#'In Python, it is strongly encouraged to use try/except blocks, to catch exceptions when we can do something about them. Let's see what that looks like.'
# try:
#     foobar
# except NameError as err:
#     print(err)
try:
    foobar #this is designed to be broken
except:
    print('PROBLEM') 
print('after the try')

#You don't want to try and catch all errors with blanket code like above. It won't actually tell you what is wrong. Unacceptable on corporate environment
#With that said, I may use it INITIALLY to catch issues that I can go back and look at with my human brain.
#Eventually, I will build the proper error codes and handling proceedures.

#To make it a bit better, do this:
try:
    foobar
except NameError:
    print('variable used never declared.')
#in this case, if there is a type of error that is not 'NameError' the try and except will not run. 
#I can write out multiple try and excepts to catch all kinds of errors without breaking code

#something a bit more useful
def get(d, key):
    try:
        d[key]
    except KeyError:
        return None

d = {'name', 'Ricky'}
print(get(d, 'name')) #this will return 'Ricky'
print(get(d, 'lame')) #this will return None and allow the code to continue
d['lame'] #this will just give a generic KeyError since 'lame' is not in dict

#211 - Try, Except, Else, Finally
#This is basically if, elif, else but for error handling
#try:
#except:
#else:
#finally: - not as commonly used as everything else

while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("Good job, you entered a number!")
		break
	finally:
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")

# try:
# 	num = int(input("please enter a number: "))
# except:
# 	print("That's not a number!")
# else:
# 	print("I'M IN THE ELSE!")
# finally:
# 	print("RUNS NO MATTER WHAT!")

# def divide(a,b):
# 	try:
# 		result = a/b
# 	except ZeroDivisionError:
# 		print("don't divide by zero please!")
# 	except TypeError as err:
# 		print("a and b must be ints or floats")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError) as err:
		print("Something went wrong!")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")



# print(divide(1,2))
print(divide(1,'a'))
print(divide(1,0))

#212 - Debugging with PDB
# FIRST EXAMPLE:
import pdb
first = "First"
second = "Second"
pdb.set_trace() #most common use of PDB. Put this before the line that you expect to break to see what is happening
result = first + second
third = "Third"
result += third
print(result)


# Be careful with variable names!
def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace() 

    return a + b + c + d
add_numbers(1,2,3,4)

# ===================
# NOTES  NOTES  NOTES
# ===================
# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list) #this will show you where you are in the code
# n (next line)
# p (print)
# c (continue - finishes debugging) #This is the BETTER way to quit the program. It will continue the code and quit when it is done
# q (quit) Use this if I don't want the code to finish running
#one more note. If I have variable names that conflict with pdb commands, the command will run. Just be careful with naming and know that you may need to change names when debugging