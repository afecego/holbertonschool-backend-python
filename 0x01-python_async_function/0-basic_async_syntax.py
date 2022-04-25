#!/usr/bin/env python3
import random


async def wait_random(max_delay: int = 10):
    """return random delay between 0 and max_delay seconds"""
    i = random.uniform(0, max_delay)
    return i
