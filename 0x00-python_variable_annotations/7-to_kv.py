#!/usr/bin/env python3
"""
7-to_kv.py
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as arguments
    and returns a tuple. The first element of the tuple
    is the string k. The second element is the square of
    the int/float v and should be annotated as a float.

    Args:
        k (str): The key for the key-value pair.
        v (Union[int, float]): The value for the key-value pair.

    Returns:
        Tuple[str, float]: A tuple containing the key and
        the square of the value.
    """
    return (k, v**2)
