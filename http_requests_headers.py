# This shows how to use headers.
# Part of video 227

# plain text
# This is great, for sites that will allow me to use it...Most will not
# It just prints out the text. Even if I was looking for pricing though, I would still only want certain text.
import requests

url = 'https://icanhazdadjoke.com/'

response = requests.get(url, headers={'Accept': 'text/plain'})

print(response.text)

# JSON
# This could be INCREDIBLY powerful. I'm not sure what useful sites I could use it on, but I'll definitely look and build if I can.
# Much simplier than scrapy, although I'd imaging I'm either doing the extra work in Scrapy or Python (if a site even has an API)
import requests

url = 'https://icanhazdadjoke.com/'

response = requests.get(url, headers={'Accept': 'application/json'})

print(response.text)  # prints the text to console without all the code
# It's a string, so would be very difficult to iterate over in a meaningful way.
print(type(response.text))
print(response.json())  # turns the JSON into Python and prints it

data = response.json()  # save response.json to variable

print(type(data))  # Shows that it is a dict, making it useful python code!

# This will print out value of key 'joke' by itself. SOOOOOO useful when taking data and translating it to larger data sets to be scrutinized (not printing it obviously)
print(data['joke'])
