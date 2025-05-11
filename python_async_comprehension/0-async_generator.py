#!/usr/bin/env python3
"""
Module implementing an asynchronous generator function.
Contains functionality for yielding random values with delays.
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Creates an asynchronous generator that produces random values.

    Yields a random float between 0 and 10 every second,
    for a total of 10 values.
    """
    for _ in range(10):
        # Pause execution for 1 second
        await asyncio.sleep(1)
        # Generate and yield a random value between 0 and 10
        yield uniform(0, 10)
