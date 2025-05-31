#!/usr/bin/env python3
"""
Helper stuff for pagination - converts page numbers to slice indexes
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Figure out which slice of data to return based on page number

    This converts from human-friendly page numbers (starting at 1)
    to Python's zero-indexed slices. Basically handles the annoying
    off-by-one conversion we always need to do.

    Returns a tuple with (start_idx, end_idx)
    """
    # The formula is simple but I always forget it:
    # skip (page-1) chunks, then take page_size items
    start = (page - 1) * page_size
    end = start + page_size

    # Note: end index in Python slices is exclusive
    return (start, end)
