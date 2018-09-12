#syntax
#regular function:
def square(num):
    return num * num
print(square(9))
#now a lambda that does same thing (can't print without it being a variable):
lambda num: num * num
#as variable
square2 = lambda num: num * num
print(square2(11))

#lambdas are basically functions with no name
#some people call them anonymous functions

#another one:
add = lambda a,b: a+b
print(add(2,4))

#something different...maybe should be in its own section...
#tkinter will help me make a GUI with Python
#I will definitely need to use this in the future!
import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

#instead of defining a function that will only be used once, it is more effient to use a lambda in the 'command' code below
# def say_hi():
#     print('HELLO!')

button = tk.Button(frame, text='CLICK ME', fg='red', command=lambda: print('Hello'))
button2 = tk.Button(frame, text='CLICK ME', fg='red', command=lambda: print('Good Bye.'))

button.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)
root.mainloop()

#END OF CODE STYLE I HAVE YET TO SEE

#Map
#a built in function to use lambdas with (common use for lambdas)
#2 arguments
#a function
#an iterable
#an iterable is something than can be iterated over (lists, strings, dictionaries, sets, tuples)
#The map runs the lambda for each value in the iterable and return a map object which can be converted into another data structure (map object)
#an example
#double everything in the list
nums = [2,4,5,6,8,10]
doubles = map(lambda x: x*2, nums)
# for num in doubles: #cannot directly print the map, so you must loop though it and print the results (not a map or list...)
#     print(num)
#OR
print(list(doubles)) #while the commented out for loop above will give the values on their own line, this will give them as a list
#VI - you can iterate over a map only once to produce values (the for loop and print(list(doubles)) will not work if run in the same program on the same map!) 


#an example with more methods(functions?)
people = ['Dan', 'Chris', 'Duc', 'Zach']

peeps = map(lambda name: name.upper(), people)
for peep in peeps:
    print(peep)

#more examples
l = [1,2,3,4]

doubles = list(map(lambda x: x*2, l))

#another
names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele'},
    {'first': 'Blue', 'last': 'Steele'},
]

first_names = list(map(lambda x: x['first'], names))
print(first_names)

#map without lambda
def double_map(x): return x*2
doubles_map = map(double_map, nums)
double_map(3)

#filter
#There is a lambda for each value in the iterable
#returns filter object which can be converted into other iterables
#The object contains only the values that return true to the lambda
#this would be useful to find non matchin pairs if the function I already discovered does not work or I want to do it using cloud computing
l = [1,2,3,4]
evens = list(filter(lambda x:x % 2 == 0, l))
evens #[2,4]

#another example:
names1 = ['al', 'beth', 'arni', 'zac']
a_names = filter(lambda n: n[0] == 'a', names1)
list(a_names) #['al', 'arni']

#another example:
#This is a more fleshed out version of the comparison function I have in mind
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

#extract inactive users using filter: #This works because the value of an empty list is inherently falsy
inactive_users = list(filter(lambda u: not u['tweets'], users))

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter: #This will find the inactive users and create an uppercase list of their usernames
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension #same as 'extract usernames of inactive users w/ map and filter:' above except less writing
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]

#list comprehension looking for names with only 5 chars:
names = ['Lassie', 'Colt', 'Rusty']
[f"Your instructor is {name}" for name in names if len(name) < 5] #['Your instructor is Colt']

#Built in functions
#all
#takes an iterable as an arguments
#returns True if all elements of the iterable are truthy (or if the iterable is empty)

all([0,1,2,3]) #False because 1,2,3 are truthy, but '0' is falsy
all([char for char in 'eio' if char in 'aeiou']) #True since all elements are truthy
all([num for num in [94,2,10,6,8] if num % 2 == 0]) #True

people = ['Char', 'Cal', 'Cody', 'Carly', 'Cristina']
all([name [0] == 'C' for name in people])
people.append('Kris')
[name [0] == 'C' for name in people] #[True, True, True, True, True, False]
all([name [0] == 'C' for name in people]) #False

#any
#very similar to all, except kinda the opposite
#Returns True if any element of the iterable is truthy. If the iterable is empty, it returns False
# see lecture 190 at 3:50 for more details

#generator functions and using sys.getsizeof
#I'm not really sure what this is (lecture 191) but it would seem to be useful if I am running into memory issues or need to hyper optimize my code
#The more I play with it, the more I DAbelieve the above statment to be the case.
#Look at the memory usage below...HUGE difference, but would not bog down any of my machines...do it 1000 times, and I might have an issue though
#The list comprehension will be useful if I need the list thereafter, whereas the generator expression would be best in all other circumstances
import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print('To do the same thing, it takes...')
print(f"List comprehension: {list_comp} bytes") #List comprehension: 9024 bytes
print(f"Generator Expression: {gen_exp} bytes") #Generator Expression: 88 bytes

#sorted
#returns a new soted list from the items in iterable
more_numbers = [6,1,8,2]
sorted(more_numbers) #[1, 2, 6, 8] sorts the list, but does not save it (unless you put it in a variable)
print(more_numbers) #[6,1,8,2] #printing the original list reveals that it is still unsorted
#note that .sort() will do the same thing, but will sort the original list
#if you need the list in reverse order:
sorted(more_numbers, reverse=True) #[8, 6, 2, 1], remember that this does not change the variable so, if you want a saved version, you must save it to new variable
#sorted also works on a tuple (it accepts them, but retruns a list)
#'Here is where it gets more powerful'
users_sort = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]
#now, say I want to sort them by user name...
#must do this:
sorted(users_sort, key=len) #will count the number of keys and sort by the longest dictionary in ascending order
sorted(users_sort, key=lambda user:user['username']) #This will sort the dictionaries in alphabetical order by usernames
sorted(users_sort, key=lambda user:len(user['tweets']) #This will sort the users by number(len) of tweets in ascending order
sorted(users_sort, key=lambda user:len(user['tweets']), reverse=True) #This will sort the users by number(len) of tweets in decending order
#Note, this is showing the syntax as wrong in Code, but when run in prompt, all is well...

#min and max

#max
#min is same, but opposite
#return the largest item in an iterable or the largest of two or more arguements.
#you can pass in, I believe, any iterable into 'max'

#max(strings, dicts with same key)
max([3,4,1,2]) #4
max([1,2,3,4]) #4
max('awesome') #'w'
max({1: 'a', 3:'c', 2:'b'}) #3
nums1 = [20,15,16,80,100]
max(nums1) #100
#min is done in the same way
min(nums1) #15
min('awesome') #'a'

names = ['bob', 'marl', 'wendy', 'doug']
min(names) #'bob'
max(names) #'wendy'
#to check by len:
min(len(name) for name in names) #3
#if I want 'bob' instead of 3, I need a lambda:
min(names, key=lambda n:len(n)) #'bob'

#this will return the min and max in a tuple:
def extremes(nums):
    return(min(nums), max(nums))

#reversed
#return a reverse iterator
nuns = [1,2,3,4]
reversed(nuns) #<list_reverseiterator object at 'memory location'
list(reversed(nuns)) #[4,3,2,1]
#If you need a list, just use .reverse()
#reversed allows you to work with the output
#example:
for char in reversed('hello world'):
    print(char) #this will give me the letters for 'hello world' in reverse order on their own lines
#I can also use a slice to get reverse (as noted much earlier in course):
'hello'[::-1] #'olleh'
#reversed is useful if I am iterating over something in reverse 

#using it on a range (see 196 around 3:15)


#len 197
#he does some review at the beginning, but I have notes
#he also gets into OOP here a bit as well. I'm going to wait for that section to take notes

#abs, sum, and round 198
#I'm going to skip this for now...Not necessarily crutial to what I need. Revisit the video if need be...
#abs()
#return the absolute value of a number. The argument can be an integer or float
#sum()
#round()

#zip
#Makes an iterator that aggregates elements from each of the iterables
#Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
#the iterator stops when the shortest input iterable is exhausted
#'okay, what it is really'
#'imagine you have 2 lists of numbers that are the same length'
#'zip will take those lists and pair up the first numbers from each list, the second, and so on'
#sounds like #not# collation in the printing world where you give the printer x copies to print and it outputs them as x copies of the first page, then x copies of the second page, and so on...
#not the best example since those pages should come out in a proper order, wheras the number sets may correlate to one another is useful ways.
#order matters
nums2 = [1,2,3,4,50]
nums3 = [6,7,8,9]
z = zip(nums2, nums3) 
list(z) #[(1, 6), (2, 7), (3, 8), (4, 9)]
z = zip(nums3, nums2) 
list(z) #[(6, 1), (7, 2), (8, 3), (9, 4)]
#notice that since the two lists were asymmetrical, it knocked off the '50' both times.
#also notice that order of variables matters (nums2, nums3) vs (nums3, nums2)
#not limited to two lists
#a better way to describe this, I think, would be to take a CSV file as an example
#a common CSV file that I use has multiple columns, and then I can do things with those columns using VB for Apps
#instead, imagine I had the same data set, but each column was broken into a different file
#I could then 'zip' them together to make a useful data set that I could then manipulate.

#video 203
#I did not do any of these exercises. I may need to in the future, but since I will mostly be working with CSV and JSV file types, it should already be done
#If I want to get into the more analytic end of the process, I will need to revisit this.
#zip to unpack a list (take it back to its root form(s))
#use the * operator
five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
list(zip(*five_by_two)) #[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)

#This is the end of zip, but I likely will need to learn it unless I plan on doing some of the 'zips' with VB for Apps (which I will likely do for now)
#I 'zip' a lot of strings together into a single column in Excel, so this is more important than I thought
