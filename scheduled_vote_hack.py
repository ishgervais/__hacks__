import requests
import asyncio

url = 'https://votes.igihe.com/rra/rra_votes.php'
myobj = {
    "poll_id": "1",
    "question_id": "10"
}

def hackVote():
    try:
        x = requests.post(url, data = myobj) 
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