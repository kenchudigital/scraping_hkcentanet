import requests
import pandas as pd

# This API using is reference from StackOverflow Answer:
# https://stackoverflow.com/questions/74272852/how-to-scrape-multiple-pages-with-the-same-url-python-3 
# However, if need to find the right API FOR WHAT DATA YOU WANT, IT NEED TO SPEND MORE TIME TO FIND IT

api_url= 'https://hk.centanet.com/findproperty/api/Transaction/Search'

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Content-Type': 'application/json'
    }

payload= {"postType":"Both","day":"Day1095","sort":"InsOrRegDate","order":"Descending","size":24,"offset":"24","pageSource":"search","gclid":"Cj0KCQjwnbmaBhD-ARIsAGTPcfVae1prjf_9aKh0dbnaBbzYvi3VhKn4qEXDAQJMS6ZvOiet8GLqzaAaAqH_EALw_wcB","q":"3qoOuFNgwUeioKQCtZ9KFA"}

lst = []
count = 0
for p in range(0, 240, 24):
    payload['offset'] = p
    res=requests.post(api_url, headers=headers, json=payload)
    for item in res.json()['data']:
        print(item)
    count = count + len(res.json()['data'])
print(f'total: {count}')


