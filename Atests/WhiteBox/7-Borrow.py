import json
import requests
import random

f = open(r'..\BlackBox\users\Users.txt','r')
users = [i + '}' for i in f.read()[1:-1].replace('\'','"').split('},')]
users[24]=users[24][:-1]
users = [json.loads(i) for i in users]

r = requests.post('http://localhost:8000/api/User/token/',json={'username':'ADz','password':'123456'})
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
print('1st Test : logged in as a user not made by signing up')
print('expected status code : 401')
req_body = {"BorrowOfferID":1}
print('starting request...')
r = requests.post('http://localhost:8000/api/Books/Book-BorrowStart/',headers=hed,json = req_body)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')

print('2nd Test : not logged in')
print('expected status code : 401')
req_body = {"BorrowOfferID":1}
print('starting request...')
r = requests.post('http://localhost:8000/api/Books/Book-BorrowStart/',json = req_body)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')
r = requests.post('http://localhost:8000/api/User/token/',json=random.choice(users))
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}

print('3rdt Test : valid user but the reqest has an invalid book id')
print('expected status code : 400')
r = requests.post('http://localhost:8000/api/User/token/',json=random.choice(users))
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
req_body = {"BorrowOfferID":243}
print('starting request...')
r = requests.post('http://localhost:8000/api/Books/Book-BorrowStart/',headers=hed,json = req_body)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')

print('4th Test : proper request')
print('expected status code : 200')
req_body = {"BorrowOfferID":1}
print('starting request...')
r = requests.post('http://localhost:8000/api/Books/Book-BorrowStart/',headers=hed,json = req_body)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')
