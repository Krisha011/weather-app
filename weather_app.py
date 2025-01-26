import requests
from prettytable import PrettyTable


from prettytable import PrettyTable

API_KEY = "1b9f5f6bffa91dd01bbc5476945d9f8c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def display_weather(data):
    table = PrettyTable()
    table.field_names = ["Parameter", "Value"]
    table.add_row(["City", data['name']])
    table.add_row(["Temperature", f"{data['main']['temp']} °C"])
    table.add_row(["Humidity", f"{data['main']['humidity']}%"])
    table.add_row(["Weather", data['weather'][0]['description']])
    print(table)

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def display_weather(data):
    table = PrettyTable()
    table.field_names = ["Parameter", "Value"]
    table.add_row(["City", data['name']])
    table.add_row(["Temperature", f"{data['main']['temp']} °C"])
    table.add_row(["Humidity", f"{data['main']['humidity']}%"])
    table.add_row(["Weather", data['weather'][0]['description']])
    print(table)

from ipywidgets import widgets
from IPython.display import display

city_input = widgets.Text(
    description="City:",
    placeholder="Enter city name"
)
display(city_input)

def on_submit(change):
    city = city_input.value
    weather_data = get_weather(city)
    if weather_data['cod'] == 200:
        display_weather(weather_data)
    else:
        print(f"City '{city}' not found. Please check the spelling.")

city_input.on_submit(on_submit)
