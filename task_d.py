import asyncio
import time

import aiohttp


def run_case(func, times, url):
    start_time = time.perf_counter()
    asyncio.run(func(times, url))
    total_time = time.perf_counter() - start_time
    print(f'Запросы: {times}; Всего времени: {total_time:.2f} с.')


async def async_gather_http_get(times: int, url: str):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(times):
            tasks.append(asyncio.create_task(session.get(url)))
        responses = await asyncio.gather(*tasks)
        return [await r.text(encoding='UTF-8') for r in responses]


if __name__ == '__main__':
    URL = 'http://httpbin.org/delay/3/'
    NUMBER_OF_REQUESTS = 100
    run_case(async_gather_http_get, NUMBER_OF_REQUESTS, URL)
