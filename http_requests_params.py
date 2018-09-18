# using the dad joke sites' API, you can pass in parameters to the URL to get specific search results.
# Either looking at the URL param changes as I search or using the API documentation
# is necessary since the params will be different for each site.

import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},  # asking for json
    # this sets term to cat and limits the output to 1 result (limit not necessary unless I want it)
    params={"term": "cat", "limit": 1}
)

data = response.json()  # saves the JSOn to a variable
print(data["results"])  # the results keyword is decided by the API
