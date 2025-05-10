#!/usr/bin/env python3
"""
Module for mixed list operations
Contains a function that calculates the sum of a list containing
both integers and floating point numbers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Args:
        mxd_lst: A list containing both integers and floating point values

    Returns:
        The total sum as a floating point number
    """
    total = 0.0
    for num in mxd_lst:
        total += num
    return total