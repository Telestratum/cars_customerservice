# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.model200_order_deleted_response import Model200OrderDeletedResponse  # noqa: E501
from swagger_server.models.model201_order_created_response import Model201OrderCreatedResponse  # noqa: E501
from swagger_server.models.model400_bad_request_response import Model400BadRequestResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model404_not_found_response import Model404NotFoundResponse  # noqa: E501
from swagger_server.models.model409_conflict_response import Model409ConflictResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server.models.order_details import OrderDetails  # noqa: E501
from swagger_server.models.order_info import OrderInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrdersController(BaseTestCase):
    """OrdersController integration test stubs"""

    def test_booking_car(self):
        """Test case for booking_car

        
        """
        body = {
                "model_id": "d2c5bca8ee9f43468c9e0e963682120b",
                "user_id": "680bec8d597c48dfa41e4eb7522756de",
                "transaction_id": "6e8626e5d1d646d0a7c1eea5377731ef",
                "offer_id": "a516894d97da4b8e8a013c5a72663e5a",
                "colour": "Cosmic Cyan"
                }
        response = self.client.open(
            '/customerservice/v1/orders',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_order(self):
        """Test case for delete_order

        
        """
        response = self.client.open(
            '/customerservice/v1/orders/{order_id}'.format(order_id='395202dea4b74f9da6a5aca1ba6b1975'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_get(self):
        """Test case for orders_get

        
        """
        response = self.client.open(
            '/customerservice/v1/orders',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
