import asyncio
import time


async def uradi():
    for i in range(10):
        print(f"Ja nesto radim {i}")
        await asyncio.sleep(1)

async def main():
    t1 = asyncio.create_task(uradi())
    t2 = asyncio.create_task(uradi())
    await asyncio.sleep(20)

asyncio.run(main())