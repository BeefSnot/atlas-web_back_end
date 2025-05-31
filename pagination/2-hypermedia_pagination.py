#!/usr/bin/env python3
"""
Module for handling pagination with hypermedia links
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Figure out which items to return based on pagination params"""
    # Formula: skip (page-1)*page_size items, then take page_size
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


class Server:
    """Server class to paginate baby names database"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # Cache the dataset to avoid re-reading the file
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Get dataset (load from file if not cached)"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Skip header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a specific page of data
        
        page: which page to fetch (starts at 1)
        page_size: how many items per page
        """
        # Make sure inputs make sense
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Figure out which slice of data we need
        idx_start, idx_end = index_range(page, page_size)

        # Get our data
        data = self.dataset()

        # Don't crash if page is too big
        if idx_start >= len(data):
            return []

        # Return the slice we want
        return data[idx_start:idx_end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get page with navigation metadata (HATEOAS-style)
        
        Returns dict with:
        - page_size: actual size of returned page
        - page: current page number
        - data: the actual page data
        - next_page: next page number or None
        - prev_page: previous page number or None
        - total_pages: how many pages total
        """
        # Get the actual page data
        page_data = self.get_page(page, page_size)

        # Figure out total pages - need ceiling division
        data_size = len(self.dataset())
        # Avoid div by zero if someone passes page_size=0 for some reason
        total_pgs = math.ceil(data_size / page_size) if page_size else 0

        # Build response with all the metadata
        return {
            'page_size': len(page_data),  # actual returned size
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pgs else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pgs
        }
