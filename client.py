import requests
url = 'http://127.0.0.1:5000/get_form'
payload = {'login_email': 'test@ex.com', 'login_password':'safhsd'}

res = requests.post(url, data=payload)

print(res.text)
