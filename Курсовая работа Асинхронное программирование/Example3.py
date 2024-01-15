import asyncio

async def my_coroutine():
    print("Coroutine is running")

async def main():
    # Создаем планировщик событий (Event Loop)
    loop = asyncio.get_event_loop()

    # Запускаем корутину в планировщике событий
    loop.create_task(my_coroutine())

    # Запускаем планировщик событий и ожидаем завершения
    await asyncio.gather(my_coroutine(), my_coroutine(), my_coroutine())

# Запускаем программу
asyncio.run(main())
