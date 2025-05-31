#!/usr/bin/env python3
"""
Module with pagination utilities - handles slicing data into pages
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start/end indexes for pagination"""
    # Basic pagination math - convert from 1-indexed pages to 0-indexed slices
    start = (page - 1) * page_size
    end = start + page_size
    
    return (start, end)


class Server:
    """Server that handles pagination of baby names dataset"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # We'll cache the data to avoid hitting the disk repeatedly
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset"""
        # Only load once
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Skip the header - first row is column names
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets a specific page from the dataset
        
        page: which page to fetch (starts at 1!)
        page_size: how many items per page
        
        Returns the slice of data for the requested page
        """
        # Sanity checks - make sure inputs are reasonable
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        # Calculate slice indexes
        start, end = index_range(page, page_size)
        
        # Get our data
        data = self.dataset()
        
        # Handle out-of-range requests gracefully
        if start >= len(data):
            return []  # empty for non-existent pages
            
        # Return the right chunk of data
        return data[start:end]
