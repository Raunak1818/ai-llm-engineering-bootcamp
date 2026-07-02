# 

import asyncio

async def brew(name):
    print(f"Brewing {name}....")
    await asyncio.sleep(2)
    print(f"{name} is ready")

async def main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Green Chai"),
        brew("Ginger Chai"),
    )

# asyncio.run(main())




# 

import asyncio

async def make_chai():
    print("Making chai...")
    await asyncio.sleep(2)
    print("Chai is ready")


async def make_coffee():
    print("Making coffee...")
    await asyncio.sleep(3)
    print("Coffee is ready")


async def main():
    await asyncio.gather(
        make_chai(),
        make_coffee(),
    )

# asyncio.run(main())



# 

import asyncio

async def cook(name):
    print(f"Cooking {name}....")
    await asyncio.sleep(2)
    print(f"{name} is ready")

async def main():
    await asyncio.gather(
        cook("Pizza"),
        cook("Burger"),
        cook("Pasta"),
    )

# asyncio.run(main())




# 

import asyncio

async def download(file):
    print(f"Downloading {file}......")
    await asyncio.sleep(2)
    print(f"{file} is downloded")

async def main():
    await asyncio.gather(
        download("File1.pdf"),
        download("File2.pdf"),
        download("File3.pdf"),
    )

asyncio.run(main())