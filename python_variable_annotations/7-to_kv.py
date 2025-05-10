#!/usr/bin/env python3
"""
Module implementing a key-value transformer function
that creates tuples with calculated values.

The module provides functionality to convert a string and a numeric value
into a tuple containing the string and the squared value.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string key and numeric value to a tuple with the squared value.

    Args:
        k: String key to be used as first element in the tuple
        v: Numeric value (int or float) to be squared

    Returns:
        A tuple containing the original string and the square of thepython_async_function
        value as a float
    """
    # Calculate square and ensure float type
    squared_value = float(v * v)
    return (k, squared_value)
