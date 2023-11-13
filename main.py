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


# Функция для позитивной проверки
def positive_assert(track):
    # Получаем заказ по его номеру и сохраняем код ответа в status_code
    status_code = get_track_by_number(track).status_code
    # Получаем заказ по его номеру и сохраняем номер трека в track_number
    track_number = get_track_by_number(track).json()['order']['track']
    # Проверяем, что код ответа равен 200
    assert status_code == 200
    # Проверяем, что номер трека совпадает
    assert track_number == track


# Тест 1. Проверяем что по треку заказа можно получить данные о заказе.
def test_create_order_by_track_success_response():
    # Вызываем функцию для позитивной проверки, передав ей номер заказ
    positive_assert(create_order())
