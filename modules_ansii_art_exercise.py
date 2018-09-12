# note, the colors are not working in this even though I brought in colorama and init() it
# not a big deal because I will likely never use it again, but wanted to mention it in case I come across this someday (windows 10)

from colorama import init
from termcolor import colored

from pyfiglet import Figlet
init()

f = Figlet(font='slant')
intend = input('What would you like to render?')
colors = input('What color?')
colored_ascii = colored(intend, color=colors)
print(f.renderText(colored_ascii))
