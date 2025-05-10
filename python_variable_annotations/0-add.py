#!/usr/bin/env python3
"""
Module providing a type-annotated addition function.
This implementation handles floating point addition with proper typing.
"""


def add(a: float, b: float) -> float:
    """
    Calculate the sum of two floating point values.

    Args:
        a: First floating point operand
        b: Second floating point operand

    Returns:
        The sum as a floating point number
    """
    return a + b