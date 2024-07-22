#!/usr/bin/env python3
"""Server class Module which fetches popular baby names from a file and
use an index_range to filter the data to be gotten per page"""

import csv
import math
from typing import List


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

    def index_range(self, page: int, page_size: int) -> tuple:
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets the page data based on the page number and the page size
        Parameter:
            page: int : page you want to start from
            page_size: int : how long you want to go into

        Returns:
            List: data from csv
        """
        # checks if both params are type int
        assert isinstance(page, int)
        assert isinstance(page_size, int)

        # Check if both params are greater than 0
        assert page_size > 0
        assert page > 0

        # Get the data of entire csv into an object
        data: list = self.dataset()

        # Create empty list to store the filtered list and use a page_range
        # to get the index_range to get the list data

        page_list: list = []
        page_range: tuple = self.index_range(page, page_size)
        for i in range(page_range[0], page_range[1]):
            if i > len(data):
                return []
            page_list.append(data[i])

        return page_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns dict containing param key value"""
        data: list = self.get_page(page, page_size)
        if data == []:
            prev_page = None
            next_page = None
        else:
            prev_page: int = page - 1
            next_page: int = page + 1

        total_pages: int = math.ceil(len(self.dataset()) / page_size)

        return {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
