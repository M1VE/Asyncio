import asyncio

async def coroutine1():
    print("Coroutine 1 started")
    await asyncio.sleep(2)
    print("Coroutine 1 finished")

async def coroutine2():
    print("Coroutine 2 started")
    await asyncio.sleep(1)
    print("Coroutine 2 finished")

async def main(): 
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    await asyncio.gather(task1, task2)

# Запуск основной функции
asyncio.run(main())

