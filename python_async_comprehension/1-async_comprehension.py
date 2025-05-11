#!/usr/bin/env python3
"""
Module implementing asynchronous list comprehension.
Demonstrates working with data from async generators.
"""
from typing import List

# Import the generator from the previous module
async_generator = __import__('0-async_generator').async_generator


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
