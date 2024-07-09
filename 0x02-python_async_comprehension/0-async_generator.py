#!/usr/bin/env python3
"""
This module demonstrates the usage of
asynchronous generators.
"""

import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields
    a random integer between 0 and 10
    after a 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
