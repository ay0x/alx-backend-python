#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of executing
    async_comprehension four times in parallel
    """
    start_time = perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time
