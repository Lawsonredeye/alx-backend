#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Parameters:
        page: int: the page being entered
        page_size: int: desired page size from the user

    Returns:
        tuple: two numbers of start index and end index for pagination
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
