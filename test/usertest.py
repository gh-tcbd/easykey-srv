import requests
payload = {'email':'tom@carrio.me','password':'testpass','first_name':'Tom','last_name':'Carrio'}
print("POST registration info to REST API")
r = requests.post('http://localhost:5000/register', data=payload)
print(r.text)
#print('Access key is {}'.format(r.json()['token']))

#print('Failed, status {}'.format(r.json()['status'])