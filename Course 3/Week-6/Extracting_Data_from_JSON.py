import requests
import json

'''
In this case, the structure of JSON is:

{
    "note":"This file contains the actual data for your assignment",
    "comments":[
        {
            "name":"Lilliarna",
            "count":100
        },
        ...
    ]
}

So, first we need to access to comments then access the count to get sum of thems
'''

url = "http://py4e-data.dr-chuck.net/comments_1249558.json"

r = requests.get(url)

datas = json.loads(r.text)

print(sum(int(data['count']) for data in datas['comments']))
