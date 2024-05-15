#!/usr/bin/env python3
'''
Redis exercise
'''


import redis
import uuid
import json
from functools import wraps
from typing import Callable, Union


def count_calls(method: Callable) -> Callable:
    '''
    count_calls decorator
    '''

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        wrapper method
        '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''
    call_history decorator
    '''

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        wrapper method
        '''
        key = method.__qualname__
        inputs = key + ":inputs"
        outputs = key + ":outputs"

        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, result)

        return result

    return wrapper


def replay(method: Callable) -> None:
    '''
    replay method
    '''
    key = method.__qualname__
    redis_db = method.__self__._redis
    inputs = redis_db.lrange(key + ":inputs", 0, -1)
    outputs = redis_db.lrange(key + ":outputs", 0, -1)

    print(f"{key} was called {redis_db.get(key)} times:")
    for input, output in zip(inputs, outputs):
        in_ans = input.decode('utf-8')
        out_ans = output.decode('utf-8')
        print(f"{key}(*{in_ans}) -> {out_ans}")



class Cache:
    '''
    Cache class
    '''
    def __init__(self):
        '''
        __init__ method
        '''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()


    def get(
        self,
        key: str,
        fn: Callable = None
    ) -> Union[str, bytes, int, float]:
        '''
        get method
        '''
        value = self._redis.get(key)
        if value is None:
            return value
        if fn is None:
            return value
        return fn(value)


    def get_str(self, key: str) -> str:
        '''
        get_str method
        '''
        return self.get(key, str)  # type: ignore


    def get_int(self, key: str) -> int:
        '''
        get_int method
        '''
        return self.get(key, int)  # type: ignore


    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        store method
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
