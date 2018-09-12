# Section 8, Part 72

# ask for age
print('How old are you?')
age = input()

if age:
    age = int(age)
    if age >= 21:
        print("You can enter and drink.")
    elif age >= 18:
        print("You can enter, but need a wristband.")
    else:
        print("You are too young.")
else:
    print("Enter an age!")

# 18-21 wristband
# 21+ drink, normal entry
# elif, too young, sorry
