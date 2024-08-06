#!/usr/bin/env python3
'''
measure the runtime of async_comprehension
'''
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    measure the runtime of async_comprehension
    """
    start = time.perf_counter()
    await async_comprehension()
    end = time.perf_counter()
    return (end - start)
