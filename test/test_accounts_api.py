# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.accounts_api import AccountsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_account(self):
        """Test case for delete_account

        Delete an account  # noqa: E501
        """
        pass

    def test_delete_all_accounts(self):
        """Test case for delete_all_accounts

        Delete all accounts  # noqa: E501
        """
        pass

    def test_edit_account(self):
        """Test case for edit_account

        Edit an account  # noqa: E501
        """
        pass

    def test_execute_sepa_direct_debit(self):
        """Test case for execute_sepa_direct_debit

        Execute SEPA Direct Debit  # noqa: E501
        """
        pass

    def test_execute_sepa_money_transfer(self):
        """Test case for execute_sepa_money_transfer

        Execute SEPA Money Transfer  # noqa: E501
        """
        pass

    def test_get_account(self):
        """Test case for get_account

        Get an account  # noqa: E501
        """
        pass

    def test_get_and_search_all_accounts(self):
        """Test case for get_and_search_all_accounts

        Get and search all accounts  # noqa: E501
        """
        pass

    def test_get_daily_balances(self):
        """Test case for get_daily_balances

        Get daily balances  # noqa: E501
        """
        pass

    def test_get_multiple_accounts(self):
        """Test case for get_multiple_accounts

        Get multiple accounts  # noqa: E501
        """
        pass

    def test_request_sepa_direct_debit(self):
        """Test case for request_sepa_direct_debit

        Request SEPA Direct Debit  # noqa: E501
        """
        pass

    def test_request_sepa_money_transfer(self):
        """Test case for request_sepa_money_transfer

        Request SEPA Money Transfer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
