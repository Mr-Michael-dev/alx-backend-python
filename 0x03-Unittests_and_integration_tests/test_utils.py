#!/usr/bin/env python3
"""This module contain test for utils
"""

import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test class to test access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any) -> None:
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
