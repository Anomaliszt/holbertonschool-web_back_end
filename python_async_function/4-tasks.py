#!/usr/bin/env python3
""" Module for the tasks function. """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.
    
    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for task_wait_random.
    
    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
