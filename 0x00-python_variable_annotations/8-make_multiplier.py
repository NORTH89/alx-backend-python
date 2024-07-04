#!/usr/bin/env python3
""" Make multiplier. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument and returns a
    function that multiplies a float by multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the product of that float and the multiplier.
    """
    def multiply(num: float) -> float:
        """
        Takes a float num as argument and returns the
        product of that float and the multiplier.

        Args:
            num (float): The float to multiply.

        Returns:
            float: The product of num and the multiplier.
        """
        return num * multiplier
    return multiply
