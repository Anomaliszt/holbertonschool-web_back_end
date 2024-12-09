#!/usr/bin/env python3
""" Measure runtime """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime and return it """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
