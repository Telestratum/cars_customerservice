import connexion
import six
import uuid
from pymongo import MongoClient
from flask import jsonify , request
import ast
import json
import logging,logging.config



from swagger_server.models.model400_bad_request_response import Model400BadRequestResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model404_not_found_response import Model404NotFoundResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server.models.transaction_details import TransactionDetails  # noqa: E501
from swagger_server.models.transaction_info import TransactionInfo  # noqa: E501
from swagger_server import util

cluster = MongoClient("localhost",27017)
carDatabase = cluster.carDatabase
transactions = carDatabase.transactions
users = carDatabase.users
car_models = carDatabase.car_models


def add_transaction(body=None):  # noqa: E501
    """add_transaction

    Add transaction # noqa: E501

    :param body: Adding transaction
    :type body: dict | bytes

    :rtype: TransactionDetails
    """
    if connexion.request.is_json:
        # body = TransactionInfo.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if users.find_one({"user_id":body['user_id']}):
                    if car_models.find_one({"model_id":body['model_id']}):
                        body.update({"transaction_id" : (uuid.uuid4().hex)})
                        transactions.insert_one(body)
                        return "transaction is made", 200
                    else:
                        return "check your model_id"
            else:
                return "check your user_id"
        except 401:
            return "unauthorized", 401
        except 403:
            return "Forbidden", 403
        except 404:
            return "Not found", 404
        except 503:
            return "server unavailable", 503
        except 500:
            return "Internal server error",500
        
def get_transactions():  # noqa: E501
    """get_transactions

    Get transactions # noqa: E501


    :rtype: TransactionDetails
    """
    try:
    
        data = transactions.find()
        data_list=[]
        for i in data:
            i["_id"]=str(i["_id"])

            data_list.append(i)
        return data_list,200
    except 401:
        return "unauthorized", 401
    except 403:
        return "Forbidden", 403
    except 404:
        return "Not found", 404
    except 503:
        return "server unavailable", 503