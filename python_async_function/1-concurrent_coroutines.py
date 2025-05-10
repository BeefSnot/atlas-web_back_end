#!/usr/bin/env python3
"""
Module for running multiple coroutines concurrently.
Demonstrates how to manage multiple async tasks.
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random multiple times in parallel.

    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay for each wait_random call

    Returns:
        List of delays in ascending order
    """
    # Using asyncio.gather for a different implementation
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
