#What is a list?
#A list is a group of items (strings, ints, floats, etc.) packaged
#together into one callable item (a list).
#Side not, a dictionary is a list of lists (will be very useful)

#basic list
tasks = ['Install Python', 'Learn Python', 'Take A Break']

#How many elements (items) exist in the list?
# For this, you will use 'len' which stands for length.
length = [1, 2,4,6]
print(len(length)) 

#Another way to make a list
#using the list function
#The variable below will ACTUALLY SHOW the range
#whereas just using 'range' creates the range,
#but does not show it...
tasks2 = list(range(1, 4))

#Accessing data in list
#First, you should know how lists perceive ranges
#Lists, like ranges, always start counting at zero. 
#So the first element in the list is at '0' (zeroith index)
friends = ['Mark', 'Taz', 'I Have No Friends']
print(friends[0]) #'Mark'
print(friends[2]) #I Have No Friends
print(friends[1]) #taz
print(friends[-2]) #print 'Taz'
#this makes 'Taz' the data for 'the_best' by pulling (copying)
#it from the list 'friends'
the_best = friends[1] 

#TO CHECK IF A VALUE IS IN A LIST (VI)
#use the word 'in'
#case matters, but I can .lower everything to make it work
#if I want to make sure
#using 'friends' list above:
'Ashley' in friends #will be False
'Taz' in friends #will be True

#VI as well!
#if statement with 'in':
if 'Taz' in friends:
    print('He is a dog, not a friend. Or he is still a friend...')
#Aside: Some psudo code for price update:
#if first_row in control and first_row in old_element_vape same
#then change price in new_element_vape

#How to access all items in a list at same time (VI):
#for loop:
numbers = [1,2,3,4]

for i in numbers:
    print(i)

#this will manipulate the value of 'i' before printing it.
for i in numbers:
    print(i*i)


#while loop:
#to use a while loop, you need to take advantage of the index in the list
#while loops will let you do things with the data..
#i guess for loops won't?
#if that is the case, I will need to use while loops
numbers = [1,2,3,4]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

#another, more complicated, while example.
#This also shows how to pull the index number AND the 
#index value in the same statement
#[] will pull the value, while {} will pull the number
colors = ['red', 'blue', 'green']
i = 0

while i < len(colors):
    print(f"{i}: {colors[i]}")
    i += 1


#List methods:
#working with llists is very common.
#there are quite a few things we can do!
#maybe add and item, split them, etc.

#side note, there is a difference between functions and methods
#think math...
#functions are global
#methods are specific to certain things, such as lists
#this is my understanding so far...
#'if we have a function attached to something, such as a list
#it is a list method, otherwise it is just a function'

#append
#add an item to the END of a list (1 argument only)
#if you try to pass another list through append,
#it will add the list to the end as a single item ([5,6,7,8])
#This adds 'Teal' to the end of the colors list in this program
colors.append('Teal')

#extend
#extend will add ALL the values you give it to the end
#of the list
#use this if you want to add more than one thing
# to THE END of a list.
#Below will add the presented values to the list colors
#AFTER 'Teal'
#Note that it will MERGE the two lists
colors.extend(['Orange', 'Purple', 'Cyan'])

#insert
#insert will insert an item at a given point
#the example below this line will insert 'Yellow'
#in the second (third since zero is first) point in list
colors.insert(2, 'Yellow')

#The example below this like will insert a list 
#at the third (fourth) point in the list colors
#note that it does not merge the lists into colors
#but will add a new list in the second (fourth) point
#in the list
colors.insert(3, ['Rum Red', 'Blood Orange', 'Sapphire'])
#Note: If I did colors.insert(-1, 'Blue')
#it would put 'Blue in the NEXT TO LAST SPOT
#because it is accounting for the old list, not the list
#after the new 'Blue value is added...
#To use insert for this noted task (could just use 'append')
# I could do:
#colors.insert(len(colors), 'Blue')
#This looks at the length of numbers and then adds to the end.
#may be useful for pricing, so I added it...

#More list methods:
#removing items from list:

#clear
#Use clear when you want to clear a list
#This removes everything from the list
#but not the list variable
numbers = [1,2,3,4,5] #create the list
numbers.clear() #clear the list
print(numbers) #print the empty list

#pop
#remove the item at the given position in the list, and return it.
#VI, If no index is specified, it removes and returns
#the last items in the list
numbers = [1,2,3,4,5]
numbers.pop() #since no index is passed, it removes '5' and returns it
numbers.pop(0) #this removes '1' and returns it
print(numbers) #This  will print the altered list:[2,3,4]

#another note on pop
#you can pass the removed value into a variable
new_list = numbers.pop(1) #This will put '3' in the variable 'new_list' instead of removing and returning

#remove
#removes the first item from the list whose value is 'x'
#Throws a ValueError if the item is not found
#'remove' does not return the value it is removing
#since you already know what it is (because you asked
# for it by name)
#Note: Depending on how I choose to do the pricing,
#this may be useful
#certainly this all will be useful for something

#The code below this line will remove the Value 2,
#not the INDEX 2 (if it did index 2, it would remove
# the VALUE 3)
list1 = [1,2,3,4,5]
list1.remove(2)

#Note that 'remove' will only remove the first value.
#In the below example, only the first instance of '2' 
#will be removed...
listx = [1,2,2,3]
listx.remove(2)

#remove with strings (case sensative I think)
list2 = ['y', 'e', 'l', 'l', 'o']
list2.remove('y') #this will remove 'y'
#Note that if 'y' is not in the list, I will get a ValueError

#More List Methods:
#Index, Count, Sort, Reverse, and Something:

#index
#index returns the index of an item within a list.
#index referring to where it is.
#Note it starts at 0...
#if you try to index something that does not exist, it will throw an error, use count in that case
numbers = [1,2,3,4,5]

numbers.index(3) #this will return '2' since 3 is at the 2 index position (remember 0)

#You can specify a start and end to the index function (method?)
numbers = [5,5,6,7,5,8,8,9,10]

numbers.index(5) #This will output 0 since '0' is the index of the number '5' (remember zero)
numbers.index(5, 1) #This will output 1 since '1' is the '1st' index of the number '5' after skipping hte first (0)(remember zero and that this skips zero index since we requested 1)
numbers.index(5, 2) #This will output 4 since '4' is the '2th' index of the number '5' (remember zero and that this skips zero and one indexes before starting its search)
numbers.index(8, 6, 8) #This is using a start AND end index. This will output 6. I am starting at 6 index and ending at 8 index. It skips the 6 at the fifth index (remember zero)

#count
#count accepts a single input and outputs the number of times the input occurs in the list
#this may be very useful to count the number of times the same product is displayed FROM the same retailer (there is a problem likely if it is more than 1)
#this could also be used to make sure everything is still included from the previous run
#example: Smok Mag was in the last run and its name is automatically added to a list
#next run, I compare the old list with the current list
#Smok Mag no longer shows up
#I'd want to look into that...
numbers = [1,2,3,4,3,2,1,4,10,2]

numbers.count(2) #outputs '3' since 2 is included in the list 3 times
numbers.count(21) #outputs '0' since 21 is not found in list
numbers.count(3) #outputs 2

#reverse
#reverse sreverses the order of the list (in place)
#in place means it is taking the list given and doing the changes there. no new list is created. BE CAREFUL
first_list = [1,2,3,4]

first_list.reverse()
print(first_list) #output [4,3,2,1]

#sort
#very breif decription here
#will get into much more detail in another section once custom functions and lambas are understood
#sort the items of the list (in-place)
#For now, no input is provides, but, as said earlier, I will once the above stuff is understood
another_list = [6,4,1,2,5]

another_list.sort()
print(another_list) #output [1,2,4,5,6]

#join
#not a list method
#different from everything else covered so far
#it is actually a string method (rather than a list method)
#it is very common in lists though to convert lists to strings
words = ['Coding', 'is', 'Fun!']
#whatever string join is called on (in the case below ' ') will be put between the strings in the list. Seems like a space would be most useful, but likely not always...
' '.join(words) #output will be a new string from the list and put the 'string' was called on (in this case a space) in the middle, 'Coding is Fun!'

#here is one where something besides a space would be useful
name = ['Mr', 'Steele']
'. '.join(name) #output string is 'Mr. Steele'
#note that join does not change the list. It will still be in tact once the join is run. It just returns whatever you ask for.
#if I want to store the output, I need to do this:
concatenated_name = '. '.join(name) #makes concatenated_name = 'Mr. Steele'

#slicing
#this can be used on lists or strings
#I will be focused on lists here
#note that this just shows the 'slice', it doesn't change the original list
#the syntax for slicing is different from what I have been doing:
#some_list[start:end:step]
#syntax similar to range...
first_list = [1,2,3,4]

first_list[1:] #[2,3,4]
first_list[3:] #[4]
first_list[1] #Note the lack of a colon. Here, it would output '1' since it is the item at the first index location. '1' is not in []

#if I wanted to create a new list from the new slice, I would do:
first_list = [1,2,3,4]

new_list = first_list[1:] #[2,3,4] in now stored in 'new_list'

#I can also use negative numbers...
first_list = [1,2,3,4]

first_list[-1:] #[4]
first_list[-3:] #[2,3,4]

#you can also easily copy a list using slicing (True, but not 'is'):
first_list = [1,2,3,4]

new_list = first_list[:] #[1,2,3,4]
new_list == first_list #True
new_list is first_list #False

#adding in an 'end' to a slice:
list1 = [1,2,3,4]

list1[:2] #output [1,2]
list1[:4] #output [1,2, 3,4]
list1[1:3] #output [2,3]
#if you pass in a negative number at the end of the slice, it will exclude that many numbers from the end (counting backwards)
list1[:-1] #[1,2,3]
list1[1:-1] #[2,3]

#now add the step
list1 = [1,2,3,4,5,6]

list1[1::2] #[2,4,6]
list1[::2] #[1,3]

#it gets a bit more complicated with negative numbers
list1[1::-1] #[2,1] #I am moving to the '1th' position and stepping back 1 at a time, giving [2,1]
list1[:1:-1] #[6,5,4,3] #In this case, I start at '2' and step back 1 at a time from the end. the '2' is excluded becasue the 'end' portion of the statement is exclusive.
list1[2::-1] #[3,2,1] #Now I am moving to the third (0,1,2) position and stepping back one at a time.

#Tricks with slices
#reversing lists/strings
string1 = 'This is fun!'

string1[::-1] #!nuf si siht #Say output as reverse in this case.

#modify specific portions of a list
numbers = [1,2,3,4,5]
numbers[1:3] = ['a', 'b', 'c']

print(numbers) #[1, 'a', 'b', 'c', 4, 5]


#swapping values
#used if you want to move a value froim one location in a list to another
names = ['James', 'Mike']

names[0], names [1] = names[1], names[0]
print(names) #['Mike', 'James']

#This is in section 13, 'List Comprehension', but it feels better here I think
#Nested Lists
#aka multidimensional lists
#I've seen these a bit previously
nested_list = [[1,2,3], [4,5,6], [7,8,9]] #This only has 3 elements since each list is an element...async def 
#When would I use nested lists?
#'More frequently than I'd expect'
#Why?
#If I'm building a game, I will use them (complex data structure (matricies))
#Game boards/mazes
#Rows and columns for visualizations, tabulation, and grouping data (ding, ding, ding)
#I'm thinking JSON inside a list such as 'mods' inside a list such as 'VapeWild'...

#Accessing nested lists:
#Note, I will need to understand how to access info by specific string AND something...I think I could make it happen with what I have so far...
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
nested_list[0][1] #output 2 #first list, second entry
nested_list[1][-1] #output 6 #Second list, last entry

#printing values or iterating through nested lists:
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
for i in nested_list:
    for val in i:
        print(val) #this will print all the values in the lists on separate lines











#OLD STUFF
colors = ["purple", "teal", "magenta", "crimson", "green", True, 1.11]

for c in colors:
    print(c)

numbers = [1, 2, 3, 99, 66, 87]

for n in numbers:
    print(n)
    print(n)
i = 0
while i < len(numbers):
    print(f"{i}: {numbers[i]}")
    i += 1

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()
print(result)

# slicing
# some_list[start:end:step]
while sounds[0:4:2]:
    print(sounds)
    break
