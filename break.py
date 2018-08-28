#break will allow you to exit a loop whenever you want.
#should be put in all while loops when testing.


# breaking a while loop
while True:
    command = input("Type 'exit' to exit: ")
    if (command == "exit"):
        break

# breaking a for loops (this program is useless, but still shows how it would be done)
for x in range(1,101):
    print(x)
    if x == 3:
        break


#This is a good way to break a loop with user input.
#If someone put in 100, it will just stop at 4 (even though
#it says 3) and then say: 'Do you even listen anymore?
times = int(input("How many times do I have to tell you? "))

for time in range(times):
    print("CLEAN UP YOUR ROOM!")
    if time >= 3:
        print("do you even listen anymore?")
        break
