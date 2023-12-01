import asyncio
from aiohttp import ClientSession
base_url ='http://httpbin.org/'
async def count():
    for i in [1,2,3,4,5,6,7,8,9,10]:
        print(i)
        await asyncio.sleep(1)
async def get_delay(seconds):
    endpoint= f'/delay/{seconds}'
    print(f'getting with {seconds} delay') 
    async with ClientSession() as sessions:
        async with sessions.get(base_url+endpoint) as response:
            response = await response.read()
            print(response)
async def main():
    await asyncio.gather(get_delay(5),count()) 
asyncio.run(main())
print("done")               
