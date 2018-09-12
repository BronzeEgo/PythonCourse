# ranges
# if I just want to print numbers, I can simply interate over a rane.
# a range is just a slice of the number line.

# python ranges come in multiple forms.
# gives you integers 0 through 6 (the count starts at 0 and is excluded)
s = range(7)
# gives you integers 1 through 7 (the last number is never included)
e = range(1, 8)

# ranges with steps
x = range(1, 10, 2)  # will give me odds from 1 to 10
y = range(7, 0, -1)  # will give me integers 7 to 1 (in that order)

# to show the range in console, use print(list(variable_name))
print(list(s))
print(list(e))
print(list(x))
print(list(y))

# for loops with ranges
for num in range(10):
    print(num)

for num in range(10, 20, 2):
    print(num)
