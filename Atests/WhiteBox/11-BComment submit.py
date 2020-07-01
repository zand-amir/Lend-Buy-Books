import json
import requests
import random

f = open('..\\BlackBox\\users\\Users.txt','r')
users = [i + '}' for i in f.read()[1:-1].replace('\'','"').split('},')]
users[24]=users[24][:-1]
users = [json.loads(i) for i in users]

print('1st Test : not logged in')
print('expected status code : 401')
print('Starting the comment request...')
r = requests.post('http://localhost:8000/api/Blog/SubmitComment/1/',json={'Title':'comment on the post', 'Text': 'the text of the comment on the post'})
print('Result :')
print(r.json())
print('status code : ' + str(r.status_code)+'\n')

print('2nd Test : logged in as a user not made by signing up')
print('expected status code : 401')
r = requests.post('http://localhost:8000/api/User/token/',json={'username':'ADz','password':'123456'})
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
print('Starting the comment request...')
r = requests.post('http://localhost:8000/api/Blog/SubmitComment/1/',json={'Title':'comment on the post', 'Text': 'the text of the comment on the post'},headers=hed)
print('Result :')
print(r.json())
print('status code : ' + str(r.status_code)+'\n')

print('3rd Test : logged in as a valid user but the request does not have a valid Post id')
print('expected status code : 400')
Auth = random.choice(users)
r = requests.post('http://localhost:8000/api/User/token/',json=Auth)
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
print('Starting the comment request...')
r = requests.post('http://localhost:8000/api/Blog/SubmitComment/243/',json={'Title':'comment on the post', 'Text': 'the text of the comment on the post'},headers=hed)
print('Result :')
print(r.json())
print('status code : ' + str(r.status_code)+'\n')

print('4th Test : proper request')
print('expected status code : 201')
Auth = random.choice(users)
r = requests.post('http://localhost:8000/api/User/token/',json=Auth)
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
print('Starting the comment request...')
r = requests.post('http://localhost:8000/api/Blog/SubmitComment/1/',json={'Title':'comment on the post', 'Text': 'the text of the comment on the post'},headers=hed)
print('Result :')
print(r.json())
print('status code : ' + str(r.status_code))
