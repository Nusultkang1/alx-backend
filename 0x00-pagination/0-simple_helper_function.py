#!/usr/bin/env python3
"""index_range that takes two integer arguments
    page and page_size.
"""
from typing import Tuple


def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing a start and end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
