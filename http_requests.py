# 225 HTTP Introduction and Crash Course
# Basics of HTTP
# He didn't talk about anything I didn't already know

# 226 - HTTP Verbs and APIs
# GET - retrieve data (visit site)
# POST - write data (comment, post, upload)
# API - Application Programming Interface
# An API allows me to get data from another application without needing to understand how the application works
# Lots of websites have APIs: GitHub, Spotify, Google, etc.

# 227 - Writing Your First Python Request
import requests
url = "https://news.ycombinator.com/"
res = requests.get(url)

print(f"your request to {url} came back w/ status code {res.status_code}")
res  # <Response [200]>
res.ok  # True
res.headers  # outputs headers
res.text  # outputs the html, etc...

# 228 Requesting JSON in Python
#'Instead of sending me HTML, send plain text or JSON, etc... (not all websites support)'
# This is done using the requests module with requests headers
# example:
import requests

response = requests.get("http://www.example.com",
                        headers={'header1': 'value1', 'header2': 'value2'})
# more from 228 in http_requests_headers.py

# 229 - Sending Requests With Params
# What is a Query String?
# A way to pass data to the server as part of a GET request
# http://www.example.com/?key1=value1&key2=value2
# I've done some of this in 'The Web Dev Bootcamp'
# see more in http_requests_params.py file


# python http_requests_dad_joke_exercise.py is the most comprehensive example of this section. I believe it was section 231
