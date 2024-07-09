#!/usr/bin/env python3
"""
A coroutine that yields random numbers asynchronously
"""
import asyncio
import random


async def async_generator():
    """
    yields random number asynchronously
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
