import requests
import os
from PIL import Image
from IPython.display import IFrame

# Get Requests

url = "https://www.ibm.com/"
r = requests.get(url)

print("Response Status: ",r.status_code,'\n')

r.request.headers # Request Header

r.request.body # Request Body

res_header = r.headers # Response Header

print(res_header["date"],'\n')

print(res_header['Content-Type'],'\n')

print(r.encoding,'\n')

print(r.text[200:300],'\n')

# We can also request content other than text 

url_pic = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

p = requests.get(url_pic)

print(p.headers['Content-Type'])

# The image must be saved using a file object 

path = os.path.join(os.getcwd(),'image.png')

with open(path,'wb')as f:
    f.write(p.content)

Image.open(path)

# Post Requests 

url_post = 'https://httbin.org/post'

payload = {'name':'Siaka','ID':'09102000'}

r_post = requests.post(url_post,data=payload)

print('Post Request body: ', r_post.request.body,'\n')
print('Get Request body: ',r.request.body,'\n')

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)



