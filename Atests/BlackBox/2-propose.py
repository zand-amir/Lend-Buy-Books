import json
import requests

f = open('users\\Users.txt','r')
users = [i + '}' for i in f.read()[1:-1].replace('\'','"').split('},')]
users[24]=users[24][:-1]
users = [json.loads(i) for i in users]

for i in users:
    r = requests.post('http://localhost:8000/api/User/token/',json=i)
    access = r.json()['access']
    hed = {'Authorization':'Bearer '+access}
    req_body = {'Offered_price': 15, 'Descriptions': i['username']+'offering the book!', 'books': ['1']}
    print('starting request...')
    r = requests.post('http://localhost:8000/api/Books/Book-propose/',headers=hed,json = req_body)
    print('result:')
    print (r.json())
