import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import json

public_property_url = "https://hk.centanet.com/findproperty/list/buy?q=pOUaBGr6EqOAIcc5Nhzew"
private_property_url = 'https://hk.centanet.com/findproperty/list/buy?q=yw2IFqnk4EmYbCU7hDZMA'

payload = {
    "postType": "Sale",
    "sort": "Ranking",
    "order": "Ascending",
    "size": 24,
    "displayTextStyle": "WebResultList",
    "offset": 24,
    "estateUsages": ["PRH"]
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Content-Type': 'application/json'}

for p in range(0, 240, 24):
    print(f"p: {p}")
    payload['offset'] = p
    r = requests.get(public_property_url, json=payload, headers=headers)
    raw_data = BeautifulSoup(r.content, 'html.parser')
    spans = raw_data.find_all('span', attrs={'class':'title-lg'})
    for span in spans:
        print(span)
    print(len(spans))
    print('----')
    print('----')

# not working...