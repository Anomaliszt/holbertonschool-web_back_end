#!/usr/bin/env python3
"""
This module contains a function that calculates the length of elements
in an iterable.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element from the input
    iterable and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
