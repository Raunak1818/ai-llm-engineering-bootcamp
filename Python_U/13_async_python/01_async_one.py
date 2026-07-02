import asyncio

async def brew_chai():
    print("Brewing chai.....")
    await asyncio.sleep(2)
    print("Chai is ready..")

# asyncio.run(brew_chai())



# 

import asyncio

async def wash_cloth():
    print("Washing clothes...")
    await asyncio.sleep(4)
    print("Clothes are clean!")

# asyncio.run(wash_cloth())



# 

import asyncio

async def cook_noodles():
    print("Cooking noodless...")
    await asyncio.sleep(5)
    print("Noodless is ready")

# asyncio.run(cook_noodles())



# 

import asyncio

async def charge_phone():
    print("Charging phone..")
    await asyncio.sleep(2)
    print("Phone charged")

# asyncio.run(charge_phone())


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


asyncio.run(make_chai())
asyncio.run(make_coffee())