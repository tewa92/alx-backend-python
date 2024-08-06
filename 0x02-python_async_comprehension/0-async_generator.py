#!/usr/bin/env python3
"""async generator"""

from typing import Generator
import asyncio
import random

async def async_generator() -> Generator[float, None, None]:
    '''Write an asynchronous coroutine called async_generator
    that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10.
    Use the random module.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
