#!/usr/bin/env python3
"""
Module for creating asyncio Tasks.
Demonstrates how to convert coroutines into Tasks.
"""
import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task from the wait_random coroutine.

    Args:
        max_delay: Maximum delay to pass to wait_random

    Returns:
        An asyncio.Task object
    """
    coro = wait_random(max_delay)
    task = asyncio.create_task(coro)
    return task
