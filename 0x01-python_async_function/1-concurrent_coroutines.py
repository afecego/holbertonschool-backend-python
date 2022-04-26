#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve written and
write an async routine called wait_n that takes in 2 int arguments"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    delay = []
    for _ in range(n):
        r = await wait_random(max_delay)
        delay.append(r)
    order = sorted(delay)
    return order
