#!/usr/bin/env python3
"""1. Async Comprehensions"""

import asyncio
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using
    async comprehension over async_generator
    """
    random_num = [random_num async for random_num in async_generator()]
    return random_num
