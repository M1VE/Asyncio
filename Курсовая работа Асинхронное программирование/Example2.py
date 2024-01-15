# Пример асинхронного кода
import asyncio

async def operation2():
    print("Operation 2")
async def operation1():
    print("Operation 1")

async def asynchronous_code():
    print("Начало")
    await operation1()
    await operation2()
    print("Конец")
asyncio.run(asynchronous_code())
