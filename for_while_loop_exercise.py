# print out a pyramid of emojis using a for and then a while loop
# print('\U0001f600')

i = 1
x = '*'
while i < 11:
    print(x*i)
    i += 1

# The emoji doesn't work...
for num in range(1, 11):
    print('*'*num)
