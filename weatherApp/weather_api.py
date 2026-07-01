from OpenWeather_API import API_KEY
import requests

def get_weather_info(city, unit="metric"):
    if not city:
        return {
            'temperature': None,
            'humidity': None,
            'description': 'No city provided.'
        }

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        return {
            'temperature': temperature,
            'humidity': humidity,
            'description': weather_description
        }

    return {
        'temperature': None,
        'humidity': None,
        'description': 'Error: Unable to fetch weather data for the specified city.'
    }
