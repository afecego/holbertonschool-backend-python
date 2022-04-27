#!/usr/bin/env python3

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    delay = []
    for _ in range(n):
        r = await task_wait_random(max_delay)
        delay.append(r)
    order = sorted(delay)
    return order
