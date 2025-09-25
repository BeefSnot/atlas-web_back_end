#!/usr/bin/env python3
"""0-simple_helper_function module.

Provides a helper to compute start and end indexes for pagination
based on 1-indexed page numbers and a page size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Compute the start and end index for pagination.

    Args:
        page: 1-indexed page number (first page is 1)
        page_size: number of items per page

    Returns:
        A tuple (start, end) representing the index range suitable for slicing.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
