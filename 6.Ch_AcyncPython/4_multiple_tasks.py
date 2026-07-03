import asyncio
import time
async def api_call(url:str,delay:int): # Corutina
    print("Fetching data from:", url)
    await asyncio.sleep(delay)
    print("Data fetched from: ",url)
    return f"orders data from {url}"
async def execution():
    time.sleep(5)
    print("Execution completed")

#third task
async def transformation():
    asyncio.sleep(4)
    print("Transformacion Completed")
async def main():
    tasks = await asyncio.gather(
        api_call("https://api.example.com/orders", 2),
        execution(),
        transformation()
    )
main()
