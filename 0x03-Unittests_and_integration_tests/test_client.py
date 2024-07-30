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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Callable) -> None:
        """Test public_repos method in GitHubOrgclient"""
        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_repos_payload

        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value =\
                    "https://api.github.com/orgs/google/repos"
            client = GithubOrgClient("google")
            result = client.public_repos()

            # Verify the result
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            # Verify the mocked methods were called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                    "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
        ({"license": {}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool) -> None:
        """Test has_license method in GithubOrgClient"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
