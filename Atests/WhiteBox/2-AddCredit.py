import random
import json
import requests

f = open('..\\BlackBox\\users\\Users.txt','r')
users = [i + '}' for i in f.read()[1:-1].replace('\'','"').split('},')]
users[24]=users[24][:-1]
users = [json.loads(i) for i in users]


print('1st Test : not logged in')
print('expected status code : 401')
a=random.randint(40,60)
print('Starting the '+str(a)+' credit charge request...')
r = requests.post('http://localhost:8000/api/User/AddCredit/',json = {"Amount":a})
print('result :')
print(r.json())
print('status code : '+str(r.status_code)+'\n')

print('2nd Test : logged in as a user not made by signing up')
print('expected status code : 401')
r = requests.post('http://localhost:8000/api/User/token/',json={'username':'ADz','password':'123456'})
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
a=random.randint(40,60)
print('Starting the '+str(a)+' credit charge request...')
r = requests.post('http://localhost:8000/api/User/AddCredit/', headers=hed,json = {"Amount":a})
print('result :')
print(r.json())
print('status code : '+str(r.status_code)+'\n')

print('3rd Test : logged in as a valid user')
print('expected status code : 200')
r = requests.post('http://localhost:8000/api/User/token/',json=random.choice(users))
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
a=random.randint(40,60)
print('Starting the '+str(a)+' credit charge request...')
r = requests.post('http://localhost:8000/api/User/AddCredit/', headers=hed,json = {"Amount":a})
print('result :')
print(r.json())
print('status code : '+str(r.status_code))
