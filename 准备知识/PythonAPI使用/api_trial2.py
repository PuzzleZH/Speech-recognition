#python
import json,requests

url = 'http://api.k780.com'
payload = {
  'app' : 'ip.local',
  'appkey' : '46255',
  'sign' : '1cc898256c8a3158fa3f409009e98b36',
  'format' : 'json',
}
r=requests.post(url,data=payload)
print(r.text)