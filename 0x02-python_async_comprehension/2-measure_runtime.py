#!/usr/bin/env python3
"""
runtime for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
async def measure_runtime() -> float:
    """ runtime"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken
