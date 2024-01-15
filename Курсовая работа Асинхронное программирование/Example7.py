import asyncio

async def async_operation():
    # Асинхронная операция, которая занимает некоторое время
    await asyncio.sleep(2)
    return "Готово!"

async def main():
    # Создаем футуру для асинхронной операции
    future = asyncio.ensure_future(async_operation())
    # Выполняем другую работу в основном потоке
    # Ожидаем завершения асинхронной операции
    result = await future
    print("Результат:", result)
# Запускаем основной цикл событий
asyncio.run(main())
