#!/usr/bin/env python3

'''
Module defines a function that collect 10 random
numbers using an async comprehensing over async_generator
'''

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collects 10 random numbers using an async comprehension
        over async_generator
    """
    return [i async for i in async_generator()]
