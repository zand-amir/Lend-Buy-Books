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
Thumbnail = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
PostImage = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
req_data = {'Title':'Blog Post','Text':'The text for this post.'}
req_files = {'ThumbnailIMG':Thumbnail,'PostIMG':PostImage}
print('starting request...')
r = requests.post('http://localhost:8000/api/Blog/CreatePost/',headers=hed,data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')

print('2nd Test : not logged in')
print('expected status code : 401')
Thumbnail = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
PostImage = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
req_data = {'Title':'Blog Post','Text':'The text for this post.'}
req_files = {'ThumbnailIMG':Thumbnail,'PostIMG':PostImage}
print('starting request...')
r = requests.post('http://localhost:8000/api/Blog/CreatePost/',data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')
r = requests.post('http://localhost:8000/api/User/token/',json=random.choice(users))
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}

print('3rd Test : valid user but the reqest has an invalid Thumbnail Image')
print('expected status code : 400') #Failed to validate Images for now
r = requests.post('http://localhost:8000/api/User/token/',json=random.choice(users))
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
Thumbnail = "Invalid entry for thumbnail"
PostImage = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
req_data = {'Title':'Blog Post','Text':'The text for this post.'}
req_files = {'ThumbnailIMG':Thumbnail,'PostIMG':PostImage}
print('starting request...')
r = requests.post('http://localhost:8000/api/Blog/CreatePost/',headers=hed,data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')

print('4th Test : valid user but the reqest has an invalid Post Image')
print('expected status code : 400') # Failed to validate Images for now
r = requests.post('http://localhost:8000/api/User/token/',json=random.choice(users))
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
Thumbnail = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
PostImage = "Invalid entry for Post Image"
req_data = {'Title':'Blog Post','Text':'The text for this post.'}
req_files = {'ThumbnailIMG':Thumbnail,'PostIMG':PostImage}
print('starting request...')
r = requests.post('http://localhost:8000/api/Blog/CreatePost/',headers=hed,data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')

print('5th Test : proper request')
print('expected status code : 201')
Thumbnail = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
PostImage = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
req_data = {'Title':'Blog Post','Text':'The text for this post.'}
req_files = {'ThumbnailIMG':Thumbnail,'PostIMG':PostImage}
print('starting request...')
r = requests.post('http://localhost:8000/api/Blog/CreatePost/',headers=hed,data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')
