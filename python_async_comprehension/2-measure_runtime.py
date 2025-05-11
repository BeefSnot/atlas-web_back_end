#!/usr/bin/env python3
"""
Module implementing asynchronous list comprehension.
Demonstrates working with data from async generators.
"""
import asyncio
import time
from typing import List

# Import the generator from the previous module
async_generator = __import__('0-async_generator').async_generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def async_comprehension() -> List[float]:
    """
    Collects random numbers using async comprehension syntax.

    Uses an async generator to produce values and collects them
    into a list using Python's async comprehension feature.

    Returns:
        A list containing 10 random float values
    """
    # Use async comprehension to gather all values from the generator
    results = [num async for num in async_generator()]
    return results


async def measure_runtime() -> float:
    """
    Measures the runtime of four concurrent async_comprehension calls.
    This function uses asyncio.gather to run the async_comprehension
    function four times concurrently and measures the total time taken.
    Returns:
        The total time taken to run the four async_comprehension calls.
        This should be approximately 10 seconds, as each call takes
        about 10 seconds to complete.
    """
    start = time.time()
    await asyncio.gather(*[asyncio.create_task(
        async_comprehension()) for _ in range(4)])
    return time.time() - start  # Hopefully, this is 10 seconds
