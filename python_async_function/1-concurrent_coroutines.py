#!/usr/bin/env python3
""" Create a function that spawns wait_random n times"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for res in await asyncio.gather(*tasks):
        for i in range(len(delays)):
            if res < delays[i]:
                delays.insert(i, res)
                break
        else:
            delays.append(res)
    return delays
