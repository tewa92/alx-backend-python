#!/usr/bin/env python3
'''
async comprehension
'''
from typing import List
from importlib import import_module as using


async_generator  = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Write an asynchronous coroutine called async_comprehension
    that takes no arguments.
    The coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random
    numbers.
    '''
    return [i async for i in async_generator()]
