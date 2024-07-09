#!/usr/bin/env python3
"""
Measure time taken to  execute async_comprehension four times in parallel
using asyncio.gather
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime and return it
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = time.perf_counter()
    total_time = end_time - start_time

    return total_time
