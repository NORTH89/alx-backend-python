#!/usr/bin/env python3

import random


async def wait_random(max_delay: int = 10) -> float:
    """ returns the float of the random delay """
    return random.uniform(0, max_delay)
