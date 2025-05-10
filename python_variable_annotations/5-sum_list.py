#!/usr/bin/env python3
"""
Module for list operations.
Contains a function that calculates the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the total of all values in a list of floats.

    Args:
        input_list: A list containing floating point values

    Returns:
        The sum of all elements as a float
    """
    result: float = 0.0
    for value in input_list:
        result += value
    return result
