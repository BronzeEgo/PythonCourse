import random
import webbrowser

rand_num = random.randint(0, 2)

if rand_num == 0:
    webbrowser.open_new_tab('www.eliquidessentials.com/eliquid')
elif rand_num == 1:
    webbrowser.open_new_tab('www.eliquidessentials.com/blog')
elif rand_num == 2:
    webbrowser.open_new_tab('www.eliquidessentials.com/brands')
