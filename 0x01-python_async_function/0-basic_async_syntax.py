#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """return random delay between 0 and max_delay seconds"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
