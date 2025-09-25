#!/usr/bin/env python3
"""3-hypermedia_del_pagination module.

Deletion-resilient hypermedia pagination utilities that ensure users
do not miss items when rows have been removed between requests.
"""

import csv
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """Return a page of data resilient to deletions.

        Args:
            index: starting index in the indexed dataset; defaults to 0
            page_size: number of items to return

        Returns:
            A dictionary with keys: index, next_index, page_size, data.
        """
        if index is None:
            index = 0
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        max_index = max(indexed.keys()) if indexed else -1
        assert index <= max_index

        data = []
        current = index
        while len(data) < page_size and current <= max_index:
            if current in indexed:
                data.append(indexed[current])
            current += 1

        next_index = current
        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index,
        }
