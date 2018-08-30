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
    print(f"{i}: {colors[i]})
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
numbers = [1,2,3,4,5]

numbers.index(3) #this will return '2' since 3 is at the 2 index position (remember 0)

#can add a staart and end point...that is where i left off











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
