#!/usr/bin/env python3
""" Make multiplier. """

from typing import Callable


def make_multiplier(multiplier: float) -> (float) -> float:
    """
    Takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        (float) -> float: A function that multiplies a float by multiplier.
    """
    def multiplier_func(num: float) -> float:
        """
        Multiplies a float by the multiplier.

        Args:
            num (float): The number to multiply.

        Returns:
            float: The result of multiplying num by multiplier.
        """
        return num * multiplier
    return multiplier_func
