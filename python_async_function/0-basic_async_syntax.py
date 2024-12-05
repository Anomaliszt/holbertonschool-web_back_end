#!/usr/bin/env python3
"""
Asynchronous coroutine module that takes in an integer argument.
This module demonstrates the basic usage of async/await.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int): The maximum delay time in seconds.
    
    Returns:
        float: The random delay time that was generated and waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
