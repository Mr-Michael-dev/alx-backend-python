#!/usr/bin/env python3
"""This module contain test for clients
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
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class to test GitHubOrgclient"""
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self,
                 org: str,
                 expected: Dict,
                 mock_get_json: Callable) -> None:
        """Test for org method in GitHubOrgclient"""
        mock_get_json.return_value = expected
        gitHubOrgClient = GithubOrgClient(org)
        self.assertEqual(gitHubOrgClient.org, expected)
        mock_get_json.assert_called_once()
