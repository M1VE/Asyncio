import asyncio

async def my_coroutine():
    print("Выполнение некоторой работы")

# Создание задачи
task = asyncio.ensure_future(my_coroutine())

# Получение цикла событий
loop = asyncio.get_event_loop()  # Определение цикла событий

# Запуск цикла событий
loop.run_until_complete(task)
