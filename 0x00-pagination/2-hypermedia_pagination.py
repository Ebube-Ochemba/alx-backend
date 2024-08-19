#!/usr/bin/env python3
"""Pagination helper module"""
import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end indexes for pagination.

    Args:
    page: Current page number (1-indexed)
    page_size: Number of items per page

    Returns:
    Tuple of (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.

        Args:
        page: Current page number (1-indexed)
        page_size: Number of items per page

        Returns:
        A list of rows corresponding to the page or
        an empty list if out of range.
        """
        page_error = "Page number must be a positive integer."
        page_size_error = "Page size must be a positive integer."

        assert isinstance(page, int) and page > 0, page_error
        assert isinstance(page_size, int) and page_size > 0, page_size_error

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a page from the dataset with hypermedia pagination information.

        Args:
        page: Current page number (1-indexed)
        page_size: Number of items per page

        Returns:
        A dictionary with pagination details.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
