# show 1 - 20
# for 4 and 13, print 'x is unlucky'
# for even numbers, print 'x is even'
# for odd numbers, print 'x is odd'

# This is one way to do it
for i in range(1, 21):
    if i == 4 or i == 13:
        print(f"{i} is unlucky")
    elif i % 2 == 1:  # modulus
        print(f'{i} is odd')
    else:
        print(f'{i} is even')


# this is another. Note the 'state' variable.
for i in range(1, 21):
    if i == 4 or i == 13:
        state = 'unlucky'
        #print(f"{i} is unlucky")
    elif i % 2 == 1:
        state = 'odd'
        #print(f'{i} is odd')
    else:
        state = 'even'
        #print(f'{i} is even')
    print(f"{i} is {state}")
