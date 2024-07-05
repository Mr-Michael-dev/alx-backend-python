#!/usr/bin/env python3
"""
Write a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
    returns a tuple
    first element of the tuple is string k
    second element is the square of the int/float v
    """
    myTuple: Tuple[str, float] = (k, v*v)

    return myTuple
