#!/usr/bin/env python3
"""
Add type annotations to the function
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any, default: Union[T, None]
                     ) -> Union[Any, T]:
    """
    Returns the value associated with the given key in the dictionary,
    or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
