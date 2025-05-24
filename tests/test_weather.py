import weather


def test_city_ru_chars():
    city = 'Москва'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '200'

    assert actual == expected

def test_city_en_chars():
    city = 'Moscow'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '200'


    assert actual == expected

def test_city_mixed_chars():
    city = 'Мockва'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '404'    # Отлов ошибки происходит в Prognoz/app.py

    assert actual == expected

def test_city_nonexistent():
    city = 'mxwoihfgaegl25'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '404'    # Отлов ошибки происходит в Prognoz/app.py

    assert actual == expected

def test_city_only_spaces():
    city = '     '
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '200'    # Значение по умолчанию на такой случай у самого API - 'Xankandi'

    assert actual == expected

def test_city_ru_space_separator():
    city = 'Санкт Петербург'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '200'

    assert actual == expected

def test_city_ru_hyphen_separator():
    city = 'Санкт-Петербург'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '200'

    assert actual == expected

def test_city_en_space_separator():
    city = 'Saint Petersburg'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '200'

    assert actual == expected

def test_city_en_hyphen_separator():
    city = 'Winston-Salem'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '200'

    assert actual == expected

def test_city_ru_mixed_register():
    city = 'МоСКвА'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '200'

    assert actual == expected

def test_city_en_mixed_register():
    city = 'moScoW'
    weather_info = weather.get_current_weather(city)
    actual = weather_info['cod']
    expected = '200'

    assert actual == expected
