# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.transaction_info import TransactionInfo  # noqa: F401,E501
from swagger_server import util


class TransactionDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, model_id: str=None, user_id: str=None, transaction_amount: float=None, _date: str=None, timing: float=None, account_from: str=None, account_to: str=None, transaction_id: str=None):  # noqa: E501
        """TransactionDetails - a model defined in Swagger

        :param model_id: The model_id of this TransactionDetails.  # noqa: E501
        :type model_id: str
        :param user_id: The user_id of this TransactionDetails.  # noqa: E501
        :type user_id: str
        :param transaction_amount: The transaction_amount of this TransactionDetails.  # noqa: E501
        :type transaction_amount: float
        :param _date: The _date of this TransactionDetails.  # noqa: E501
        :type _date: str
        :param timing: The timing of this TransactionDetails.  # noqa: E501
        :type timing: float
        :param account_from: The account_from of this TransactionDetails.  # noqa: E501
        :type account_from: str
        :param account_to: The account_to of this TransactionDetails.  # noqa: E501
        :type account_to: str
        :param transaction_id: The transaction_id of this TransactionDetails.  # noqa: E501
        :type transaction_id: str
        """
        self.swagger_types = {
            'model_id': str,
            'user_id': str,
            'transaction_amount': float,
            '_date': str,
            'timing': float,
            'account_from': str,
            'account_to': str,
            'transaction_id': str
        }

        self.attribute_map = {
            'model_id': 'model_id',
            'user_id': 'user_id',
            'transaction_amount': 'transaction_amount',
            '_date': 'date',
            'timing': 'timing',
            'account_from': 'account_from',
            'account_to': 'account_to',
            'transaction_id': 'transaction_id'
        }
        self._model_id = model_id
        self._user_id = user_id
        self._transaction_amount = transaction_amount
        self.__date = _date
        self._timing = timing
        self._account_from = account_from
        self._account_to = account_to
        self._transaction_id = transaction_id

    @classmethod
    def from_dict(cls, dikt) -> 'TransactionDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The transaction_details of this TransactionDetails.  # noqa: E501
        :rtype: TransactionDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def model_id(self) -> str:
        """Gets the model_id of this TransactionDetails.


        :return: The model_id of this TransactionDetails.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id: str):
        """Sets the model_id of this TransactionDetails.


        :param model_id: The model_id of this TransactionDetails.
        :type model_id: str
        """
        if model_id is None:
            raise ValueError("Invalid value for `model_id`, must not be `None`")  # noqa: E501

        self._model_id = model_id

    @property
    def user_id(self) -> str:
        """Gets the user_id of this TransactionDetails.


        :return: The user_id of this TransactionDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this TransactionDetails.


        :param user_id: The user_id of this TransactionDetails.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def transaction_amount(self) -> float:
        """Gets the transaction_amount of this TransactionDetails.


        :return: The transaction_amount of this TransactionDetails.
        :rtype: float
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount: float):
        """Sets the transaction_amount of this TransactionDetails.


        :param transaction_amount: The transaction_amount of this TransactionDetails.
        :type transaction_amount: float
        """
        if transaction_amount is None:
            raise ValueError("Invalid value for `transaction_amount`, must not be `None`")  # noqa: E501

        self._transaction_amount = transaction_amount

    @property
    def _date(self) -> str:
        """Gets the _date of this TransactionDetails.


        :return: The _date of this TransactionDetails.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date: str):
        """Sets the _date of this TransactionDetails.


        :param _date: The _date of this TransactionDetails.
        :type _date: str
        """

        self.__date = _date

    @property
    def timing(self) -> float:
        """Gets the timing of this TransactionDetails.


        :return: The timing of this TransactionDetails.
        :rtype: float
        """
        return self._timing

    @timing.setter
    def timing(self, timing: float):
        """Sets the timing of this TransactionDetails.


        :param timing: The timing of this TransactionDetails.
        :type timing: float
        """

        self._timing = timing

    @property
    def account_from(self) -> str:
        """Gets the account_from of this TransactionDetails.


        :return: The account_from of this TransactionDetails.
        :rtype: str
        """
        return self._account_from

    @account_from.setter
    def account_from(self, account_from: str):
        """Sets the account_from of this TransactionDetails.


        :param account_from: The account_from of this TransactionDetails.
        :type account_from: str
        """

        self._account_from = account_from

    @property
    def account_to(self) -> str:
        """Gets the account_to of this TransactionDetails.


        :return: The account_to of this TransactionDetails.
        :rtype: str
        """
        return self._account_to

    @account_to.setter
    def account_to(self, account_to: str):
        """Sets the account_to of this TransactionDetails.


        :param account_to: The account_to of this TransactionDetails.
        :type account_to: str
        """

        self._account_to = account_to

    @property
    def transaction_id(self) -> str:
        """Gets the transaction_id of this TransactionDetails.


        :return: The transaction_id of this TransactionDetails.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id: str):
        """Sets the transaction_id of this TransactionDetails.


        :param transaction_id: The transaction_id of this TransactionDetails.
        :type transaction_id: str
        """

        self._transaction_id = transaction_id