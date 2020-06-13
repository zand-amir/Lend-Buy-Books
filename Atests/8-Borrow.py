import json
import requests

f = open('users\\Users.txt','r')
users = [i + '}' for i in f.read()[1:-1].replace('\'','"').split('},')]
users[24]=users[24][:-1]
users = [json.loads(i) for i in users]

j=0
for i in users:
    print('Starting the log-in request...')
    r = requests.post('http://localhost:8000/api/User/token/',json=i)
    access = r.json()['access']
    print('Log-in successful!')
    hed = {'Authorization':'Bearer '+access}
    Offer_ID = 25 - j
    j+=1
    print('Borrowing the book ' + str(Offer_ID) + '...')
    r = requests.post('http://localhost:8000/api/Books/Book-BorrowStart/',json={"BorrowOfferID":Offer_ID},headers=hed)
    print(r.json())
    
