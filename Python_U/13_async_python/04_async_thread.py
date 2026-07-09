import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} in store")
    time.sleep(3)
    return f"{item} stock:42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)

# asyncio.run(main())



# 


import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def fetch_users(user_id):
    print(f"fetching {user_id}")
    time.sleep
    return f"User -- {user_id} "

async def main():

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, fetch_users, 101)
        print(result)

# asyncio.run(main())



# 

def download_file(name):
    print(f"downloading {name}")
    time.sleep(3)
    return f"{name} downloaded"

async def main():

    files = ["a.pdf", "b.pdf", "c.pdf"] 

    # task = [asyncio.to_thread(download_file, file) for file in files]

    # result = await asyncio.gather(*task)
    # print(result)

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        task = [loop.run_in_executor(pool, download_file, file) for file in files]
        result = await asyncio.gather(*task)
        print(result)


# asyncio.run(main())






# 



def genrate_report(report_name):
    print(f"Generating {report_name}.....")
    time.sleep(3)
    return f"{report_name} ready"

async def main():
    reports = ["a.pdf", "b.pdf", "c.pdf"]

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        task = [loop.run_in_executor(pool, genrate_report, report) for report in reports]
        result = await asyncio.gather(*task)
        print(result)

# asyncio.run(main())



import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def fetch_user(item):
    print(f"publishing {item}....")
    time.sleep(2)
    return f"{item} is ready"


async def main():

    articles = ["1. article", "2. article", "3. article"]

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        task = [loop.run_in_executor(pool, fetch_user, article) for article in articles]
        result = await asyncio.gather(*task)
        print(result)

asyncio.run(main())