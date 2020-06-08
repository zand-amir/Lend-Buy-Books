import random
import json
import string
import requests

f = open('names\\IranianNames.txt','r')
names = f.read().split(',')
f.close()

Users = []

for i in range(25):
    User_data = {}
    User_data['first_name'] = random.choice(names)
    while True:
        n = random.choice(names)
        if not (n[-1] in ['a','e','h','i','o','u','y']):
            User_data['last_name'] = n+'y'
            break

    User_data['username'] = 'user no.' + str(i+1)
    User_data['password'] = '123456'
    User_data['email'] = 'user' + str(i+1) + '@emailprovider.com'
    User_data['address'] = ''.join(random.choices(string.ascii_lowercase+'     ',k=45)).replace('  ',' ').replace('  ',' ').replace('  ',' ')
    User_data['postal_code']=''.join(random.choices(string.digits,k=9))
    User_data['phone_number']=''.join(random.choices(string.digits,k=9))
    Users.append(User_data)

print('....Ready to request.......')
for i in Users:
    print("Request :")
    print(i)
    r = requests.post('http://localhost:8000/api/User/sign-up/',json=i)
    print('*************')
    print("Status : "+str(r.status_code))
    print('JSON : ' + str(r.json()))
    print("*************")
    
f = open('users\\Users.txt','w')
f.write(str(Users))
f.close()
