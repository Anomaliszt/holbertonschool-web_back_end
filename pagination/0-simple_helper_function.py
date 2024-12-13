#!/usr/bin/env python3
"""description: a function named index_range that"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    description: a function named index_range that
    takes two integer arguments page and page_size.
    """
    return (page_size * (page - 1), page * page_size)
