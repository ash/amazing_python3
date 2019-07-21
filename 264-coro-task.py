# An async coroutine
import asyncio
import time

async def myf():
    print('Enter')
    time.sleep(2)
    print('Exit')

async def main():
    print('before')
    task = asyncio.create_task(myf())
    print('after')

asyncio.run(main()) # with ()