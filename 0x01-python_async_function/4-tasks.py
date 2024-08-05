#!/usr/bin/env python3
"""
Display the average run time.
"""
from typing import List
import asyncio

task_wait_random = __import__('1-concurrent_coroutines').task_wait_random


async def measure_time(n: int, max_delay: int) -> List[float]:
    """
    Display the average run time. total_time
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
