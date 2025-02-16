#!/usr/bin/env python3
"""Type annotations"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Type-annotated function element_length that takes a list"""
    return [(i, len(i)) for i in lst]
