from flask import Flask, render_template, request
from weather import get_current_weather

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Проверяет, что введённое значение города не пустая строка или пробел, и при срабатывании ставит значение по умолчанию ('Москва')
    if not bool(city.strip()):
        city = 'Москва'

    weather_data = get_current_weather(city)

    # Если город не найден в API
    print(weather_data['cod'])
    if not weather_data['cod'] == '200':
        return render_template('not_found.html')

    return render_template('weather.html',
                           name=weather_data['city']['name'],
                           status=weather_data['list'][0]['weather'][0]['description'].capitalize(),
                           temp=f"{weather_data['list'][0]['main']['temp']:.1f}",
                           feels_like=f"{weather_data['list'][0]['main']['feels_like']:.1f}",
                           status_tmr=weather_data['list'][8]['weather'][0]['description'].capitalize(),
                           temp_tmr=f"{weather_data['list'][8]['main']['temp']:.1f}",
                           feels_like_tmr=f"{weather_data['list'][8]['main']['feels_like']:.1f}",
                           status_2tmr=weather_data['list'][16]['weather'][0]['description'].capitalize(),
                           temp_2tmr=f"{weather_data['list'][16]['main']['temp']:.1f}",
                           feels_like_2tmr=f"{weather_data['list'][16]['main']['feels_like']:.1f}")


if __name__ == '__main__':
    app.run()
