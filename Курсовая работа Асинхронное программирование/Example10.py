import asyncio
async def fetch_data(url):
    print(f"Fetching data from {url}")
    # Здесь мог бы быть асинхронный код для получения данных, например, с использованием aiohttp
    await asyncio.sleep(1)
    return f"Data from {url}"
async def process_data(data):
    print(f"Processing data: {data}")
    # Здесь мог бы быть асинхронный код для обработки данных
    await asyncio.sleep(1)
    return f"Processed data: {data}"
async def main():
    # Список URL-адресов для запросов
    urls = ["http://example.com", "http://example.org", "http://example.net"]
    # Создание списка задач для параллельного выполнения
    tasks = [fetch_data(url) for url in urls]
    # Параллельное выполнение задач с использованием asyncio.gather
    data_list = await asyncio.gather(*tasks)
    # Обработка данных
    processed_data = [await process_data(data) for data in data_list]
    # Вывод результатов
    print("Final results:")
    for result in processed_data:
        print(result)
# Запуск асинхронной программы
asyncio.run(main())

