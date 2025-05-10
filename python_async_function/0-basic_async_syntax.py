#!/usr/bin/env python3
"""
Module demonstrating basic asynchronous programming concepts.
Contains a function that creates a delay using asyncio.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random time.

    Args:
        max_delay: Maximum delay time in seconds (default: 10)

    Returns:
        The actual time delayed as a float
    """
    # Using uniform instead of random for slightly different implementation
    wait_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time