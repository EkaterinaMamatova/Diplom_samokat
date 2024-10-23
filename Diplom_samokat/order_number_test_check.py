#Екатерина Маматова, 22 кагорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request
from sender_stand_request import post_new_order, get_order_number


#Проверка автотеста

def test_order_and_status():
    response = post_new_order(data.order_body)
    track_number = response.json()["track"]

    order_response = get_order_number(track_number)

    assert order_response.status_code == 200
