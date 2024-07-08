#!/usr/bin/env python3
"""
An asynchronous coroutine named wait_random that takes in an integer argument
waits for a random delay between 0 and max_delay seconds
and returns the random integer
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds
    return a random integer
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
