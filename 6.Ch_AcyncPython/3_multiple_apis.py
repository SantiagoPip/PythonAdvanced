import time
import asyncio

async def api_call(url:str,delay:int): # Corutina
    print("Fetching data from:", url)
    await asyncio.sleep(delay)
    return f"orders data from {url}"
async def execution():
    time.sleep(5)
    

async def main():
    # Creating task with Gather
    urls_delay = [("https://api.example.com/orders", 2), ("https://api.example.com/products", 1), ("https://api.example.com/customers", 3)]
    tasks2 = [api_call(url,delay) for url,delay in urls_delay]
    results = await asyncio.gather(*tasks2)
    for result in results:
        print(result)   

asyncio.run(main())
# asyncio.run(execute2())