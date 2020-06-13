import json
import requests
import random

f = open('users\\Users.txt','r')
users = [i + '}' for i in f.read()[1:-1].replace('\'','"').split('},')]
users[24]=users[24][:-1]
users = [json.loads(i) for i in users]

Book_IDs = [i['id'] for i in requests.get('http://localhost:8000/api/Books/Books-View/').json()['This is list of all Books ']]
print('Logging in as a user')
access = requests.post('http://localhost:8000/api/User/token/',json=users[0]).json()['access']
hed = {'Authorization':'Bearer '+access}
print('Successful!')

for i in Book_IDs:
    print('Getting information...')
    book = requests.get('http://localhost:8000/api/Books/BookAdvancedSearch/?id='+str(i),headers = hed).json()[0]
    print('Book '+book['Title']+' `s comments:')
    
    coms = requests.post('http://localhost:8000/comments/ViewComments/',headers = hed,json={'BookID':i}).json()['Comments']
    for comment in coms:
        print('*********************************************************************')
        print(comment['auth'])
        print('    ' + comment['text'])
        print('*********************************************************************')

    print('______________________________________________________________________________________________________________________________________')
    
    
