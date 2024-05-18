#!/usr/bin/env python3
'''
web cache tracker
'''


import redis
import requests
from typing import Callable
from functools import wraps


def get_page(url: str) -> str:
    '''
    get_page function
    '''
    r = redis.Redis()
    key = f"count:{url}"
    r.incr(key)
    r.expire(key, 10)

    return requests.get(url).text
