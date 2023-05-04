# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.model400_bad_request_response import Model400BadRequestResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model404_not_found_response import Model404NotFoundResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server.models.transaction_details import TransactionDetails  # noqa: E501
from swagger_server.models.transaction_info import TransactionInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransactionsController(BaseTestCase):
    """TransactionsController integration test stubs"""

    def test_add_transaction(self):
        """Test case for add_transaction

        
        """
        body = {
                "model_id": "d2c5bca8ee9f43468c9e0e963682120b",
                "user_id": "680bec8d597c48dfa41e4eb7522756de",
                "transaction_amount": 200000,
                "date": "24/4/2023",
                "timing": 4.12,
                "account_from": "user5",
                "account_to": "dealer1"
                }
        response = self.client.open(
            '/customerservice/v1/transactions',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    # def test_get_transactions(self):
    #     """Test case for get_transactions

        
    #     """
    #     response = self.client.open(
    #         '/customerservice/v1/transactions',
    #         method='GET')
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
