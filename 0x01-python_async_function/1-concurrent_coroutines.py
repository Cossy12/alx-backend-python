#!/usr/bin/env python3
""" def wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-bas_async_syntax').wait_random
async def wait_n(n: int, max_delay: int) -> List[float]:
    """_summ_
    Args:
        n (int): _description_
        max_delay (int): _description_
    Ret:
        List[float]: _description_
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
