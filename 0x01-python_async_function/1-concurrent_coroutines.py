#!/usr/bin/env python3
"""
concurrent coroutines
"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Write an asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits
    """
    wait_times = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )
    return sorted(wait_times)
