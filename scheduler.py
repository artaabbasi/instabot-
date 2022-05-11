import requests


request = requests.get("http://api3.madtalk.ir:81/instagram/auto_intract/")
with open('auto_log.log', 'w') as f:
    f.write(request.status_code)
