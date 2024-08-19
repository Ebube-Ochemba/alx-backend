#!/usr/bin/env python3
"""Pagination helper module"""


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
