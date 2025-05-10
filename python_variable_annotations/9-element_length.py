#!/usr/bin/env python3
"""
Module for sequence operations.
Contains a function that computes the length of each element in an iterable.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable.

    Args:
        lst: An iterable containing sequence elements

    Returns:
        A list of tuples where each tuple contains an element from
        the input and its length
    """
    return [(element, len(element)) for element in lst]
