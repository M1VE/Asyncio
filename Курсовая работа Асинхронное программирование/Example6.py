import asyncio

i = 0

async def my_coroutine():
    try:
        while True:
            if asyncio.current_task().cancelled():
                return
            print(i)
            await asyncio.wait_for(asyncio.sleep(1), timeout=1)
    except asyncio.CancelledError:
        # Доступ к состоянию задачи с помощью 'task.get_state()'
        task = asyncio.current_task()  # Получить текущую задачу
        state = task.get_state()  # Получить состояние задачи
        # Обработать информацию о состоянии по мере необходимости

async def main():
    my_task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(5)
    my_task.cancel()

asyncio.run(main())
