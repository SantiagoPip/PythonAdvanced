import time
def api_call():
    time.sleep(2)  # Simulate a delay of 2 seconds
    return "API response"
def execute():
    print("Starting API call...")
    result = api_call()  # This will block the execution for 2 seconds
    print("API call completed.")
#execute()

import asyncio

async def api_call2():
    await asyncio.sleep(2)  # Simulate a delay of 2 seconds
    return "API response"

async def execute2():
    print("Starting API call...")
    result =  await api_call2()  # This will not block the execution for 2 seconds
    print("API call completed.",result)

asyncio.run(execute2())