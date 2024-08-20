#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page from the dataset with deletion-resilient
        pagination information.

        Args:
        page: Current page number (1-indexed)
        page_size: Number of items per page

        Returns:
        A dictionary with pagination details.
        """
        page_error = "Page number must be a positive integer."
        page_size_error = "Page size must be a positive integer."

        assert index is not None and isinstance(index, int) and index >= 0, \
            page_error
        assert isinstance(page_size, int) and page_size > 0, page_size_error

        indexed_data = self.indexed_dataset()

        if index >= len(indexed_data):
            raise AssertionError("Index out of range")

        data = []
        current_index = index

        while len(data) < page_size and current_index < len(indexed_data):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = (
            current_index if current_index < len(indexed_data) else None
        )

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
