#!/usr/bin/env python3
"""
Measure an approximate elapsed time for runing an async code
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time taken to run wait_n n times with the specified max_delay
    return the time in seconds
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time

    return total_time / n
