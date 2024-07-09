#!/usr/bin/env python3
"""
This module demonstrates the usage of
asynchronous generators.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    Returns an asynchronous generator.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
