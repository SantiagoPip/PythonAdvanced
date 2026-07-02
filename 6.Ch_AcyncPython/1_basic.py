import asyncio
import time
#croutine
async def main():
    print("!Hello, World!")  # This will print immediately
    asyncio.sleep(2) # This will not block the event loop, but it won't actually pause execution either
    print("!Hello, World2!") #  This will print immediately after the first print statement, without waiting for 2 seconds
asyncio.run(main())

async def main_2():
    print("!Hello, World!")  # This will print immediately
    await asyncio.sleep(2) # This will pause execution for 2 seconds without blocking the event loop
    print("!Hello, World2!") #  This will print immediately after the first print statement, without waiting for 2 seconds
asyncio.run(main_2())