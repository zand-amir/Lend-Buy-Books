import json
import requests
import random

f = open('users\\Users.txt','r')
users = [i + '}' for i in f.read()[1:-1].replace('\'','"').split('},')]
users[24]=users[24][:-1]
users = [json.loads(i) for i in users]

Book_IDs = [i['id'] for i in requests.get('http://localhost:8000/api/Books/Books-View/').json()['This is list of all Books ']]

for i in Book_IDs:
    for j in range(15):
        Auth = random.choice(users)
        print('Loging in as ' + str(Auth['username']) + ' ...')
        r = requests.post('http://localhost:8000/api/User/token/',json=Auth)
        access = r.json()['access']
        print('Log-in successful!')
        hed = {'Authorization':'Bearer '+access}
        print('Starting the comment request...')
        r = requests.post('http://localhost:8000/comments/SubmitComment/',json={"Comment_text":Auth['username']+'`s comment on the book with the ID of '+str(i),'BookID':i},headers=hed)
        print('Result :')
        print(r.json())
