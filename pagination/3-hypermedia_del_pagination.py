#!/usr/bin/env python3
"""
Deletion-resilient pagination implementation
"""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # private dataset attributes
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches dataset from CSV file"""
        # Only load the dataset once
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Skip the header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Creates an indexed version of the dataset"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # Unused variable - but keeping for compatibility
            truncated_dataset = dataset[:1000]
            # Build a dict with position as key
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Gets a page of data that works even if items were deleted.
        
        If items are deleted between requests, this method ensures
        we don't miss any data or have duplicates.
        """
        # Get the indexed data
        data_dict = self.indexed_dataset()
        
        # Default to beginning if no index given
        if index is None:
            index = 0
        
        # Make sure the index makes sense
        assert index >= 0 and index < len(data_dict)
        
        results = []
        next_idx = index
        counter = 0
        
        # Keep going until we have enough items or run out
        while counter < page_size and next_idx < len(self.dataset()):
            # Skip over deleted entries
            if next_idx in data_dict:
                results.append(data_dict[next_idx])
                counter += 1
            next_idx += 1
        
        # Package everything up
        return {
            'index': index,
            'data': results,
            'page_size': len(results),
            'next_index': next_idx
        }
