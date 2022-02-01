import requests
import time

url = 'https://api.karisimbi.events/api/nominee/vote'
myobj = {
    "awardId": "61ec3a81787ff108528e02bb",
    "nomineeId": "61ee8e65a95126c1ce6de41f"
}


for num in range(1,40000):
    try:
        x = requests.post(url, data = myobj)
        print(num)
        print(x.text)
    except:
        print(x.status_code)
    
