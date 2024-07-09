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
    for _  in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
        
    
if __name__ == "__main__":
    asyncio_generator = __import__('0-async_generator').async_generator
    
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)
        
    asyncio.run(print_yielded_values())
