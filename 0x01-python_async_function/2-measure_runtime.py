#!/usr/bin/env python3

import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average time per coroutine
    execution for wait_n(n, max_delay).

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average time per coroutine
        execution (total_time / n).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return (end_time - start_time) / n
