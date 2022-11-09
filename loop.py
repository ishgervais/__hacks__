import asyncio

loop = asyncio.get_event_loop()

def callback():
    print("callback")
    loop.call_later(5, callback)

loop.call_later(1, callback)

async def main():
    while True:
        await asyncio.sleep(1)

loop.run_until_complete(main())