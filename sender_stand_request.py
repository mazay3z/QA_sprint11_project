import requests
import configuration
import data


# Функция создания заказа
def create_order():
    # Отправляем запрос на создание заказа и возвращаем номер трека заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_URL, json=data.order_body).json()['track']


# Функция получения заказа
def get_track_by_number(track):
    # Получаем заказ по его номеру и возвращаем его
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_URL + str(track))