#!/usr/bin/env python3
"""
Module for running multiple tasks concurrently.
Similar to concurrent_coroutines but using Tasks.
"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random multiple times.

    Args:
        n: Number of tasks to create
        max_delay: Maximum delay for each task

    Returns:
        List of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []

    for completed in asyncio.as_completed(tasks):
        result = await completed
        results.append(result)

    return sorted(results)
