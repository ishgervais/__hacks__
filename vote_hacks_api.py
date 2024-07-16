import requests
import time

url = ''
req = {
    "awardId": '',
    "nomineeId": ''
}
limit = 10

for num in range(1,limit):
    try:
        x = requests.post(url, data = req)
        print(num)
        print(x.text)
    except:
        print(x.status_code)
    
