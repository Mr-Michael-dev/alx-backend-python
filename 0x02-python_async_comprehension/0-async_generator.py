#!/usr/bin/env python3
"""
A coroutine that yields random numbers asynchronously
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    yields random number asynchronously
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
