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
