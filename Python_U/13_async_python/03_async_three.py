# # How it works
# session.get(url) → sends a request to the API.
# await response.json() → converts the JSON response into a Python dictionary.
# data["title"] → gets only the title of the post.
# asyncio.gather(*tasks) → runs all three requests concurrently and collects the returned titles into a list



import asyncio
import aiohttp


# 

async def fetch_url(url, session):
    async with session.get(url) as response:
        print(f"fetch {url} with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        task = [fetch_url(url, session) for url in urls]
        await asyncio.gather(*task)

# asyncio.run(main())






# 


async def fetch_url(url, session):
    async with session.get(url) as response:
        print(f"fetching {url}.. with status {response.status}")

async def main():
    urls = [
    "https://example.com",
    "https://python.org",
    "https://httpbin.org/get"
]
    async with aiohttp.ClientSession() as session:
        task = [fetch_url(url, session) for url in urls]
        await asyncio.gather(*task)


# asyncio.run(main())




# 


async def get_url(url, session):
    async with session.get(url) as response:
        print(f"getting url..{url} with status {response.status}")

async def start():
    urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
]
    async with aiohttp.ClientSession() as session:
        task = [get_url(url, session) for url in urls]
        await asyncio.gather(*task)

# asyncio.run(start())





# 3: Print Response Length


async def get_url(url, session):
    async with session.get(url) as response:
        text = await response.text()
        print(f"{url} ----- {len(text)}")

async def execute():
    urls = [
        "https://example.com",
        "https://python.org",
        "https://httpbin.org/get"
    ]
    async with aiohttp.ClientSession() as session:
        task = [get_url(url, session) for url in urls]
        await asyncio.gather(*task)

# asyncio.run(execute())





# 


async def fetch_url(url, session):
    async with session.get(url) as response:
        return response.status
    
async def main():
    urls = ["https://example.com"] * 3
    async with aiohttp.ClientSession() as session:
        task = [fetch_url(url, session) for url in urls]
        result = await asyncio.gather(*task)
        print(result)

# asyncio.run(main())






# 5. Fetch User Names



async def fetch_url(url, session):
    async with session.get(url) as response:
        data = await response.json()
        return data["name"]
    
async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/users/1",
        "https://jsonplaceholder.typicode.com/users/2",
        "https://jsonplaceholder.typicode.com/users/3"
    ]
    async with aiohttp.ClientSession() as session:
        task = [fetch_url(url, session) for url in urls]
        result = await asyncio.gather(*task)
        print(result)

# asyncio.run(main())







# 6: Handle Errors



async def fetch_url(url, session):
    try:
        async with session.get(url) as response:
            print(f"{url} ------> {response.status}")
    except Exception:
        print(f"failed to fetch {url}")

async def main():
    urls = [
        "https://python.org",
        "https://abcxyz1234.com",
        "https://example.com"
    ]
    async with aiohttp.ClientSession() as session:
        task = [fetch_url(url, session) for url in urls]
        await asyncio.gather(*task)

# asyncio.run(main())






# 7: Measure Time

import time

async def fetch_url(url, session):
    async with session.get(url) as response:
        return response.status
    
async def main():
    urls = ["https://httpbin.org/delay/2"] * 5

    start = time.time()

    async with aiohttp.ClientSession() as session:
        task = [fetch_url(url, session) for url in urls]
        await asyncio.gather(*task)


    end = time.time()

    print(f"Finished in {end - start:.2f} second")

# asyncio.run(main())






# 8: Mini Website Checker



async def fetch_url(url, session):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print(f"{url} ----> UP")
            else:
                print(f"{url} --------> Down, status -{response.status}")
    except Exception:
        print(f"{url} -----> Downn")


async def main():
    urls = [
        "https://google.com",
        "https://github.com",
        "https://python.org",
    ]

    async with aiohttp.ClientSession() as session:
        task = [fetch_url(url, session) for url in urls]
        await asyncio.gather(*task)

# asyncio.run(main())





# 


async def fetch_url(url, session):
    try:
        async with session.get(url) as response:
            return response.status == 200
    except Exception:
        return False
    
async def main():
    urls = ["https://httpbin.org/get"] * 10
    async with aiohttp.ClientSession() as session:
        task = [fetch_url(url, session) for url in urls]
        result = await asyncio.gather(*task)

        success_count = sum(result)
        print(f"{success_count} requests succeeded")

asyncio.run(main())