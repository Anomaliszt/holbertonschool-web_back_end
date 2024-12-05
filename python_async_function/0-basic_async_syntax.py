#!/usr/bin/env python3
"""
Asynchronous coroutine module that takes in an integer argument.
This module demonstrates the basic usage of async/await syntax in Python.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
    
    Args:
        max_delay (int): The maximum delay time in seconds. Defaults to 10.
    
    Returns:
        float: The random delay time that was generated and waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
