# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.order_details import OrderDetails  # noqa: F401,E501
from swagger_server import util


class Model200OrderDeletedResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: int=200, message: str='ok', data: List[OrderDetails]=None):  # noqa: E501
        """Model200OrderDeletedResponse - a model defined in Swagger

        :param code: The code of this Model200OrderDeletedResponse.  # noqa: E501
        :type code: int
        :param message: The message of this Model200OrderDeletedResponse.  # noqa: E501
        :type message: str
        :param data: The data of this Model200OrderDeletedResponse.  # noqa: E501
        :type data: List[OrderDetails]
        """
        self.swagger_types = {
            'code': int,
            'message': str,
            'data': List[OrderDetails]
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'data': 'data'
        }
        self._code = code
        self._message = message
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'Model200OrderDeletedResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The 200OrderDeletedResponse of this Model200OrderDeletedResponse.  # noqa: E501
        :rtype: Model200OrderDeletedResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this Model200OrderDeletedResponse.


        :return: The code of this Model200OrderDeletedResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this Model200OrderDeletedResponse.


        :param code: The code of this Model200OrderDeletedResponse.
        :type code: int
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this Model200OrderDeletedResponse.


        :return: The message of this Model200OrderDeletedResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Model200OrderDeletedResponse.


        :param message: The message of this Model200OrderDeletedResponse.
        :type message: str
        """

        self._message = message

    @property
    def data(self) -> List[OrderDetails]:
        """Gets the data of this Model200OrderDeletedResponse.


        :return: The data of this Model200OrderDeletedResponse.
        :rtype: List[OrderDetails]
        """
        return self._data

    @data.setter
    def data(self, data: List[OrderDetails]):
        """Sets the data of this Model200OrderDeletedResponse.


        :param data: The data of this Model200OrderDeletedResponse.
        :type data: List[OrderDetails]
        """

        self._data = data
