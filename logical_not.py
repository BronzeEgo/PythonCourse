#This is about chaining operators
#See and_or.py for 'and' and 'or' logical operators
print("How old are you?")
age = int(input())
#2-8 2 dollar ticket
#65 5 dollar ticket
#10 dollar ticket for all else

#How would I do this?!
#if not int:
    #print("Type a number...")
if not ((age >= 2 and age <= 8) or age >=65):
    print("You pay $10!")
else:
    print("You are not child or senior...See receptionist...")