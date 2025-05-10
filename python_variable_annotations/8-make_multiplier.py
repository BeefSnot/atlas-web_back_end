#!/usr/bin/env python3
"""
Module for function generators.
Contains a function that creates a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies its input by a fixed multiplier.

    Args:
        multiplier: The fixed value to multiply by

    Returns:
        A function that takes a float and returns that value multiplied
        by the original multiplier
    """
    def multiply_function(x: float) -> float:
        """Inner function that performs the multiplication"""
        return x * multiplier

    return multiply_function
