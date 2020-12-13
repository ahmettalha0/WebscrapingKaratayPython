import requests
# sitenin header bilgilerini gösteren get requesti
req = requests.get("http://ahmettalha.net")
print(req.headers)
req.status_code

# json içeriği üzerinde get isteği
req_json = requests.get("https://jsonplaceholder.typicode.com/users")
print(req_json.text)

# params
req_params = requests.get("http://ahmettalha.net", params={"lesson":"python", "subject":"requests module"})
req_params.url

# post işlemi, gönderilen verinin json içeriğinden seçilip ekranda gösterilmesi
req_post = requests.post("https://httpbin.org/post", data = {"lesson":"python", "subject":"requests module"})
print(req_post.status_code)
print(req_post.text)
print(req_post.json()["form"])

# put işlemi için post işlemine benzer bir örnek
req_put = requests.put("https://httpbin.org/put", data = {"lesson":"python", "subject":"requests module"})
print(req_put.text)

# delete işlemi
req_delete = requests.delete("https://httpbin.org/delete", data = {"user_name":"Talha"})
print(req_delete.text)

# authentication konusunda requests modülü
from requests.auth import HTTPDigestAuth 
url = 'https://httpbin.org/digest-auth/auth/talha/talha123'
requests.get(url, auth=HTTPDigestAuth('talha', 'talha123'))

# session işlemi
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
s = requests.Session()
s.auth = ('talha', 'talha123')
s.headers.update({'x-test': 'true'})
print(s.headers)
print(s.auth)

req_request_object = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
req_request_object.request.headers