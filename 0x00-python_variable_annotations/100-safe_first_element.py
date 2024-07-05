#!/usr/bin/env python3
"""The types of the elements of the input are not know"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of the list, or None if the list is empty."""
    if lst:
        return lst[0]
    else:
        return None
