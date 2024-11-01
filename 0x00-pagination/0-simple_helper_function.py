#!/usr/bin/env python3

"""
Module for 0. Simple helper function.

"""


def index_range(page: int, page_size: int):
    """Calculates the range of indexes to return in a pagination system."""
    first_index = page_size * (page - 1)
    return (first_index, first_index + page_size)
