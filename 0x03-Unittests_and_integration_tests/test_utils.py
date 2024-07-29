#!/usr/bin/env python3
"""This module contain test for utils
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test access_nested_map with exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class to test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self,
                      test_url: str,
                      expected: Dict,
                      mock_get: Callable) -> None:
        """Test get_json"""
        mock_get.return_value.json.return_value = expected
        self.assertEqual(get_json(test_url), expected)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test class to test memoize"""
    def test_memoize(self) -> None:
        """Test memoize"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        @patch('TestClass.a_method')
        def test_a_method(mock_a_method: Callable) -> None:
            """Test a_method"""
            test_object = TestClass()
            mock_a_method.return_value = 43
            self.assertEqual(test_object.a_property, 43)
            self.assertEqual(test_object.a_property, 43)
            mock_a_method.assert_called_once()
