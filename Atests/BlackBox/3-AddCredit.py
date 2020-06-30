import random
import json
import requests

f = open('users\\Users.txt','r')
users = [i + '}' for i in f.read()[1:-1].replace('\'','"').split('},')]
users[24]=users[24][:-1]
users = [json.loads(i) for i in users]

for i in users:
    print('Starting the log-in request...')
    r = requests.post('http://localhost:8000/api/User/token/',json=i)
    access = r.json()['access']
    print('Log-in successful!')
    hed = {'Authorization':'Bearer '+access}
    a=random.randint(40,60)
    print('Starting the '+str(a)+' credit charge request...')
    r = requests.post('http://localhost:8000/api/User/AddCredit/', headers=hed,json = {"Amount":a})
    print(r.json())



