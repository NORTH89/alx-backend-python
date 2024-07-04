#!/usr/bin/env python3
""" Element length. """
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Takes a list of strings as argument and returns a list of
    tuples. Each tuple contains a string from the input list and
    the length of that string.

    Args:
        lst (List[str]): The list of strings to process.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing the
        strings from the input list and their lengths.
    """
    return [(i, len(i)) for i in lst]
