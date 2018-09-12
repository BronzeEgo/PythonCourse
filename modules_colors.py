# This is a note on ANSI for Windows. If I want any cool effects in the prompt, I need to download and import 'colorama' to the env I'm using.
# Colorama is the shit
# I may actually have use for termcolor when dealing with error handling. If I can force specific colors/effects on certain things, they will jump out at me better.

from termcolor import colored
from colorama import init
init()

text = colored("HI THERE!", color="magenta",
               on_color="on_cyan", attrs=["blink"])
print(text)
