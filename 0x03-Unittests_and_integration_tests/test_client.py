#!/usr/bin/env python3
"""This module contain test for clients
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self) -> None:
        """Test _public_repos_url method"""
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as mock_org:
            url = "https://api.github.com/orgs/google/repos"
            repos_url = {'repos_url': url}
            mock_org.return_value = repos_url
            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, url)
            mock_org.assert_called_once()
