#!/usr/bin/env python3
'''
Redis exercise
'''


import redis
import uuid
import json
from typing import Callable, Union


class Cache:
    '''
    Cache class
    '''
    def __init__(self):
        '''
        __init__ method
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        store method
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


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
        return self.get(key, fn=lambda x: x.decode())


    def get_int(self, key: str) -> int:
        '''
        get_int method
        '''
        return self.get(key, fn=lambda x: int(x))


    def count_calls(method: Callable) -> Callable:
        '''
        count_calls decorator
        '''
        key = method.__qualname__

        def wrapper(self, *args, **kwargs):
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapper


    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        store method
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def call_history(method: Callable) -> Callable:
        '''
        call_history decorator
        '''
        key = method.__qualname__

        def wrapper(self, *args, **kwargs):
            '''
            wrapper method
            '''
            inputs = key + ":inputs"
            outputs = key + ":outputs"
            self._redis.rpush(inputs, str(args))
            output = method(self, *args, **kwargs)
            self._redis.rpush(outputs, str(output))
            return output

        return wrapper


    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        store method
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def replay(self, method: Callable) -> str:
        '''
        replay method
        '''
        key = method.__qualname__
        inputs = key + ":inputs"
        outputs = key + ":outputs"
        input_list = self._redis.lrange(inputs, 0, -1)
        output_list = self._redis.lrange(outputs, 0, -1)

        result = f"{key}\n"
        for i, o in zip(input_list, output_list):
            result += f"Inputs: {i.decode()}\nOutputs: {o.decode()}"
        return result


    def replay_store(self) -> str:
        '''
        replay_store method
        '''
        return self.replay(self.store)


if __name__ == "__main__":
    cache = Cache()
    cache.store("hello")
    cache.store(5)
    cache.store(1.0)
    print(cache.replay_store())
    print(cache._redis.keys("*"))
    print(cache._redis.lrange("store:inputs", 0, -1))
