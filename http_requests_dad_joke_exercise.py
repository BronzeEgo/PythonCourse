# The user provides a topic to the program.
# The program makes a request to the dad joke site to get the jokes
# If there are more than one jokes, the program tells the user there are moer, and gives them one of them.
# the program quits

import requests
import pyfiglet
import termcolor
from random import choice
from colorama import init
init()

header = pyfiglet.figlet_format("Dad Joke 3000")
header = termcolor.colored(header, color="cyan")
print(header)

term = input("Let me tell you a joke! Give me a topic: ")
response_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": term}
).json()  # Putting .json here makes the response_json variable come back as json. this is simpler than declaring a new variable outside this one and passing the .json property to it(such as data = response_json.json())
results = response_json["results"]
total_jokes = response_json["total_jokes"]
if total_jokes > 1:
    print(
        f"I've got {total_jokes} jokes about {term}. Here's one:\n",
        choice(results)['joke']
    )
elif total_jokes == 1:
    print(
        f"I've got one joke about {term}. Here it is:\n",
        results[0]['joke']
    )
else:
    print(f"Sorry, I don't have any jokes about {term}! Please try again.")
