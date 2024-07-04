#!/usr/bin/env python3
""" Make multiplier. """

from typing import Callable


def create_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a given number by a given multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that multiplies a
        number by the multiplier.
    """
    def multiply_number(number: float) -> float:
        """
        Multiplies a number by the given multiplier.

        Args:
            number (float): The number to multiply.

        Returns:
            float: The result of multiplying the number by the multiplier.
        """
        return number * multiplier

    return multiply_number
