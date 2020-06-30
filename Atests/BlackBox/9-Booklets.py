import json
import requests
import PyPDF2

f = open('users\\Users.txt','r')
users = [i + '}' for i in f.read()[1:-1].replace('\'','"').split('},')]
users[24]=users[24][:-1]
users = [json.loads(i) for i in users]

for i in users:
    r = requests.post('http://localhost:8000/api/User/token/',json=i)
    access = r.json()['access']
    hed = {'Authorization':'Bearer '+access}
    pdf = open(r'C:\Users\Lenovo\Desktop\SE1.pdf','rb')
    image = open(r'C:\Users\Lenovo\Desktop\Untitled.png','r')
    req_data = {'Title':i['username']+' offer','Category':'بدون دسته بندی' ,'Description': 'Some description for the offer', 'Course_name': 'The booklet`s course','University_name':'IUST','Professor_name':'Ashtiani M.','Semester':'panj'}
    req_files = {'PDF':pdf,'Image':image}
    print('starting request...')
    r = requests.post('http://localhost:8000/api/Booklets/CreateBooklet/',headers=hed,data=req_data,files=req_files)
    print('result:')
    print (r.json())
