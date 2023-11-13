from sender_stand_request import get_track_by_number, create_order


# Функция для позитивной проверки
def positive_assert(track):
    # Получаем заказ по его номеру и сохранем ответ
    response = get_track_by_number(track)
    # Cохраняем код ответа в status_code
    status_code = response.status_code
    # Cохраняем номер трека в track_number
    track_number = response.json()['order']['track']
    # Проверяем, что код ответа равен 200
    assert status_code == 200
    # Проверяем, что номер трека совпадает
    assert track_number == track


# Тест 1. Проверяем что по треку заказа можно получить данные о заказе.
def test_create_order_by_track_success_response():
    # Вызываем функцию для позитивной проверки, передав ей номер заказ
    positive_assert(create_order())
