#!/usr/bin/env python3
"""
Module for testing GithubOrgClient class
This contains test cases for the GithubOrgClient
"""
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

org_payload = TEST_PAYLOAD[0][0]
repos_payload = TEST_PAYLOAD[0][1]
expected_repos = TEST_PAYLOAD[0][2]
apache2_repos = TEST_PAYLOAD[0][3]

class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient
    Contains unit tests for the GithubOrgClient class methods
    """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        and that get_json is called with the expected URL
        
        Args:
            org_name: Name of the organization to test
            mock_get_json: Mock object for get_json function
        """

        expected = {"login": org_name, "id": 123}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url returns the URL
        based on the mocked org property
        """

        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test-org/repos"
            }
            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            self.assertEqual(result, "https://api.github.com/orgs/test-org/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        """

        expected = [{"name": "repo1", "private": False},
                    {"name": "repo2", "private": False},
                    {"name": "repo3", "private": False},
                    {"name": "repo4", "private": False},
                    {"name": "repo5", "private": False},]
        
        mock_get_json.return_value = expected

        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock) as mock_url:

            mock_url.return_value = "https://mock.url"
            client = GithubOrgClient("test-org")
            result = client.public_repos()

            expected_repos = [repo["name"] for repo in expected]

            self.assertEqual(result, expected_repos)
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://mock.url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license correctly identifies
        if a repo has a specific license
        
        Args:
            repo: Repository dictionary with license information
            license_key: License key to check for
            expected: Expected result of the check
        """
        client = GithubOrgClient("test-org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)

@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [(org_payload, repos_payload, expected_repos, apache2_repos)]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient class
    Tests actual API responses with fixtures
    """
    
    @classmethod
    def setUpClass(cls):
        """
        Set up class method to prepare for integration tests
        Creates a patcher for requests.get
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        
        def side_effect(url):
            """Side effect function to mock different responses"""
            mock_response = Mock()
            
            if url == "https://api.github.com/orgs/google":
                mock_response.json.return_value = cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                mock_response.json.return_value = cls.repos_payload
            
            return mock_response
            
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to clean up after integration tests
        Stops the patcher
        """
        cls.get_patcher.stop()
    
    def test_public_repos(self):
        """
        Test that GithubOrgClient.public_repos returns the expected list of repos
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
    
    def test_public_repos_with_license(self):
        """
        Test that GithubOrgClient.public_repos with license filter works correctly
        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
