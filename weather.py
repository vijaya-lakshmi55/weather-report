import httpx
from datetime import datetime

temperature_list = []  # creating empty list to store data
locations_name = []


def weather():  # weather() is defined under this function url will collect the data according to user input
    try:
        # client = httpx.Client(timeout=None)
        Location_name = input("Enter the Location name: ").upper()
        apikey_1 = "af8085b321f6c4faf90c2d93c3d4518c"
        url_1 = f'https://api.openweathermap.org/data/2.5/weather?q={Location_name}&appid={apikey_1}'
        res1 = httpx.get(url_1)
        data1 = res1.json()

        url_2 = 'https://wttr.in/{}?format= Moon face:%m'.format(Location_name)
        res_2 = httpx.get(url_2)
        a = res_2.text

        apikey_3 ="418c1f8bff764fe2b9c388274b213e51"
        url_3 ='https://api.weatherbit.io/v2.0/current?'
        full_url = url_3 + "&key=" + apikey_3 + "&city=" + Location_name
        res3 = httpx.get(full_url)
        data3 = res3.json()

        date = datetime.now().date()
        time = datetime.now().time().strftime("%H:%M:%S")
        locations_name.append(Location_name)
    # wind_speed,sky_description from url_1
        wind_speed = data1['wind']['speed']
        Sky_Description = data1['weather'][0]['description']
    # temperature,wind_dir from url_2
        temperature = (data3['data'][0]['temp'])
        temperature_list.append(temperature)
        wind_dir = (data3['data'][0]['wind_cdir_full'])

        return {
            "Date": date,
            "Time": time,
            "Location_name": Location_name,
            "Wind speed": wind_speed,
            "Sky description": Sky_Description,
            "moon face": a,
            "temp":temperature,
            "wind direction":wind_dir

        }
    except KeyError:   # to avoid key_error
        print("Location not found! Try again")
