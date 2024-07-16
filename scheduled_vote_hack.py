import requests
import asyncio

url = ''
req = {
    "poll_id": "",
    "question_id": ""
}

def hackVote():
    try:
        x = requests.post(url, data = req) 
        # print(num)
        print(x.text)
    except:
        print(x.status_code)

loop = asyncio.get_event_loop()

def callback():
    hackVote()
    loop.call_later(605, callback)

loop.call_later(1, callback)

async def main():
    while True:
        await asyncio.sleep(1)

loop.run_until_complete(main())