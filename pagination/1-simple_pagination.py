#!/usr/bin/env python3
"""1-simple_pagination module.

Defines a Server class to paginate Popular_Baby_Names.csv using
simple page and page_size parameters.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Compute the start and end index for pagination.

    Args:
        page: 1-indexed page number (first page is 1)
        page_size: number of items per page

    Returns:
        Tuple (start, end) suitable for slicing a list.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Reads the CSV once and caches rows excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset.

        Args:
            page: 1-indexed page number (default 1)
            page_size: number of items per page (default 10)

        Returns:
            A list of rows for the requested page; empty list if out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(data):
            return []
        return data[start:end]
