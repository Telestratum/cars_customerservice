import connexion
import six
import uuid
from pymongo import MongoClient
from flask import jsonify , request
import ast
import json
import logging,logging.config


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
from swagger_server import util

cluster = MongoClient("localhost",27017)
carDatabase = cluster.carDatabase
car_orders = carDatabase.car_orders
car_models = carDatabase.car_models
transactions = carDatabase.transactions

logging.basicConfig(filename="newfile2.log",format="%(filename)s::%(levelname)s:%(message)s",level=logging.DEBUG)


def booking_car(body=None):  # noqa: E501
    """booking_car

    Book a car # noqa: E501

    :param body: Booking cars
    :type body: dict | bytes

    :rtype: Model201OrderCreatedResponse
    """
    if connexion.request.is_json:
        # body = OrderInfo.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if car_orders.find_one({"transaction_id":body['transaction_id']}):
                    return "car already booked for this transaction"
                
            else:
                    if transactions.find_one({"transaction_id":body['transaction_id']}):
                        body.update({"order_id" : (uuid.uuid4().hex)})
                        car_orders.insert_one(body)
                        return "order is created", 201
                    else:
                        return "transaction id is Not Found",404
                
        except:
            return "Internal_server_error",500


def delete_order(order_id):  # noqa: E501
    """delete_order

    delete order # noqa: E501

    :param order_id: 
    :type order_id: str

    :rtype: Model200OrderDeletedResponse
    """
    try:
        
        if car_orders.find_one({"order_id":order_id}):
            car_orders.delete_one({"order_id":order_id})
            return "successfully deleted",200
        else:
            return "order_id is Not Found", 404

    except:
        return "Internal_server_error",500

def orders_get():  # noqa: E501
    """orders_get

    Get  all users # noqa: E501


    :rtype: OrderDetails
    """
    try:
    
        data = car_orders.find()
        data_list=[]
        for i in data:
            i["_id"]=str(i["_id"])

            data_list.append(i)
        return data_list,200
    except:
         return "Internal_server_error",500
