#!/usr/bin/env python3
"""
Redis cache module implementation
"""
import redis
import uuid
from typing import Union


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
