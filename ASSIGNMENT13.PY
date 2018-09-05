#Q1

import requests
target=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
data=target.json()
print(data['quoteText'])
