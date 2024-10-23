#Екатерина Маматова, 22 кагорта — Финальный проект. Инженер по тестированию плюс
from requests import Response

import configuration
import requests
import data


#Запрос на создание заказа

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


#Запрос на получения заказа по треку заказа

def get_order_number(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response
