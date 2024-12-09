#!/usr/bin/env python3
""" Asnyc comprehension """
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
        """
        Collect 10 random numbers using
        an async comprehensing over async_generator 
        """
        return [number async for number in async_generator()]
