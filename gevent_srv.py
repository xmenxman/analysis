import time
import asyncio

async def acc(n):
    result = 1
    for i in range(n, 1, -1):
        print(f"{result} + {i}")
        result += i
        time.sleep(0.01)
    print(f"->{n}的累加结果是：{result}")

# acc(800)
# acc(500)
acc(100)
asyncio.open_connection()

# import asyncio
#
#
# @asyncio.coroutine
# def get_body(i):
#     print('start{}'.format(i))
#     yield from asyncio.sleep(1)
#     print('end{}'.format(i))
#
#
# loop = asyncio.get_event_loop()
# tasks = [get_body(i) for i in range(5)]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
