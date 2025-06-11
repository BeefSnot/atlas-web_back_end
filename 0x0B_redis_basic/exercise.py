#!/usr/bin/env python3
"""
Redis cache module implementation
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called
    
    Args:
        method: The method to decorate
        
    Returns:
        Decorated method that counts calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to record the history of inputs and outputs for a function
    
    Args:
        method: The method to decorate
        
    Returns:
        Decorated method that records call history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(inputs_key, str(args))
        
        output = method(self, *args, **kwargs)
        
        self._redis.rpush(outputs_key, output)
        
        return output
    return wrapper


class Cache:
    """
    Redis-based caching class that provides storage functionality
    """
    def __init__(self):
        """
        Initialize Redis client and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random key
        
        Args:
            data: The data to store (string, bytes, int, or float)
            
        Returns:
            The randomly generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, 
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and convert to desired format
        
        Args:
            key: The key to look up
            fn: Optional conversion function
            
        Returns:
            The data in the desired format or None if key doesn't exist
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve string data from Redis
        
        Args:
            key: The key to look up
            
        Returns:
            The data as a string or None if key doesn't exist
        """
        return self.get(key, lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve integer data from Redis
        
        Args:
            key: The key to look up
            
        Returns:
            The data as an integer or None if key doesn't exist
        """
        return self.get(key, int)
