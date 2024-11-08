#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from math import ceil
from typing import List, Dict


def index_range(page: int, page_size: int):
    """Calculates the range of indexes to return in a pagination system."""
    first_index = page_size * (page - 1)
    return (first_index, first_index + page_size)


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
        """"""
        index = 0 if index is None else index

        total_pages = ceil(len(self.dataset()) / page_size)
        assert index >= 0 and index <= total_pages - 1
        keys = list(self.indexed_dataset().keys())[
            index: index + page_size]
        return {
            "index": index,
            "data": list(map(lambda x: self.indexed_dataset()[x], keys)),
            "next_index": index + page_size
        }
