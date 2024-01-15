import asyncio

async def foo():
    print("Start foo")
    await asyncio.sleep(2)
    print("End foo")

async def bar():
    print("Start bar")
    await asyncio.sleep(1)
    print("End bar")

async def main():
    print("Start main")
    await asyncio.gather(foo(), bar())
    print("End main")

if __name__ == "__main__":
    asyncio.run(main())
