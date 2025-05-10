#!/usr/bin/env python3
"""
Module providing mathematical operations.
Contains a function that returns the floor of a floating point number.
"""
import math


def floor(n: float) -> int:
    """
    Calculate the floor of a floating point number.

    Args:
        n: The input floating point number

    Returns:
        The largest integer less than or equal to the input
    """
    return math.floor(n)