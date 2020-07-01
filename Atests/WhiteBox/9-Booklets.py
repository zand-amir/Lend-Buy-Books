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
pdf = open(r'C:\Users\Lenovo\Desktop\SE1.pdf','rb')
image = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
req_data = {'Title':'booklet','Category':'بدون دسته بندی' ,'Description': 'Some description for the offer', 'Course_name': 'The booklet`s course','University_name':'IUST','Professor_name':'Ashtiani M.','Semester':'panj'}
req_files = {'PDF':pdf,'Image':image}
print('starting request...')
r = requests.post('http://localhost:8000/api/Booklets/CreateBooklet/',headers=hed,data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')

print('2nd Test : not logged in')
print('expected status code : 401')
pdf = open(r'C:\Users\Lenovo\Desktop\SE1.pdf','rb')
image = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
req_data = {'Title':'booklet','Category':'بدون دسته بندی' ,'Description': 'Some description for the offer', 'Course_name': 'The booklet`s course','University_name':'IUST','Professor_name':'Ashtiani M.','Semester':'panj'}
req_files = {'PDF':pdf,'Image':image}
print('starting request...')
r = requests.post('http://localhost:8000/api/Booklets/CreateBooklet/',data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')
r = requests.post('http://localhost:8000/api/User/token/',json=random.choice(users))
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}

print('3rd Test : valid user but the reqest has an invalid PDF File')
print('expected status code : 400')
r = requests.post('http://localhost:8000/api/User/token/',json=random.choice(users))
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
pdf = "Invalid entry as a PDF File"
image = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
req_data = {'Title':'booklet','Category':'بدون دسته بندی' ,'Description': 'Some description for the offer', 'Course_name': 'The booklet`s course','University_name':'IUST','Professor_name':'Ashtiani M.','Semester':'panj'}
req_files = {'PDF':pdf,'Image':image}
print('starting request...')
r = requests.post('http://localhost:8000/api/Booklets/CreateBooklet/',headers=hed,data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')

print('4th Test : valid user but the reqest has an invalid Image File')
print('expected status code : 400') # Failed to validate the image for now
r = requests.post('http://localhost:8000/api/User/token/',json=random.choice(users))
access = r.json()['access']
hed = {'Authorization':'Bearer '+access}
pdf = open(r'C:\Users\Lenovo\Desktop\SE1.pdf','rb')
image = "Invalid entry as an Image"
req_data = {'Title':'booklet','Category':'بدون دسته بندی' ,'Description': 'Some description for the offer', 'Course_name': 'The booklet`s course','University_name':'IUST','Professor_name':'Ashtiani M.','Semester':'panj'}
req_files = {'PDF':pdf,'Image':image}
print('starting request...')
r = requests.post('http://localhost:8000/api/Booklets/CreateBooklet/',headers=hed,data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')

print('5th Test : proper request')
print('expected status code : 201')
pdf = open(r'C:\Users\Lenovo\Desktop\SE1.pdf','rb')
image = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
req_data = {'Title':'booklet','Category':'بدون دسته بندی' ,'Description': 'Some description for the offer', 'Course_name': 'The booklet`s course','University_name':'IUST','Professor_name':'Ashtiani M.','Semester':'panj'}
req_files = {'PDF':pdf,'Image':image}
print('starting request...')
r = requests.post('http://localhost:8000/api/Booklets/CreateBooklet/',headers=hed,data=req_data,files=req_files)
print('result:')
print (r.json())
print('status code : ' + str(r.status_code)+'\n')
