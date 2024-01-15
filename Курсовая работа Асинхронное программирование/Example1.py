import asyncio
async def operation2():
    print("Operation 2")
async def operation1():
    print("Operation 1")

# Пример синхронного кода
def synchronous_code():
    print("Начало")
    operation1()
    operation2()
    print("Конец")

synchronous_code()
'''В данном примере наш код не выполняет какую либо функцию, но
если мы подставим вместо operation1 и operation 2 подставим 
любые две функции они будут выполняться в указанном нами порядке '''