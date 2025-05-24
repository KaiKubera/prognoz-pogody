from dotenv import load_dotenv
import requests
import os
from pprint import pprint

load_dotenv()


def get_current_weather(city='Москва', units='metric'):
    """
    city = название города, прогноз которого требуется найти. Возможен ввод на русском и английском языках (пр.: 'Москва', 'Ulan-Ude')

    units = единицы измерения, в которых возвращаются значения прогноза (градусы по Цельсию или по Фаренгейту). Доступны метрическая ('metric') и имперская ('imperial') системы
    """
    request_url = f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={os.getenv("API_KEY")}&q={city}&units={units}&lang=ru'
    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == '__main__':
    print('\n/// Узнать прогноз погоды ///\n')
    city = input('Введите название города: ')

    # Проверяет, что введённое значение города не пустая строка или пробел, и при срабатывании ставит значение по умолчанию ('Москва')
    if not bool(city.strip()):
        city = 'Москва'

    weather_data = get_current_weather(city)
    print('\n')
    pprint(weather_data)
