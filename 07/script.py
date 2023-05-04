import argparse
import asyncio
import aiohttp


async def fetch_url(session, url, concurrency):
    semaphore = asyncio.Semaphore(concurrency)
    async with semaphore:
        async with session.get(url) as response:
            html = await response.text()
            semaphore.release()
            return html, url


async def fetch_urls(session, urls, concurrency):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(fetch_url(session, url, concurrency))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    return result


async def main(urls, concurrency):
    async with aiohttp.ClientSession() as session:
        data = await fetch_urls(session, urls, concurrency)
    for lenght, url in data:
        print(f"Fetched {len(lenght)} bytes from {url}")
    return data


if __name__ == "__main__":
    with open("urls.txt", "r") as f:
        urls = f.read().strip().split(", ")

    asyncio.run(main(urls, 5))
