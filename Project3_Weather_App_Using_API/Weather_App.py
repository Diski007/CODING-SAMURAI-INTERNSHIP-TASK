import requests

city_name = "Lagos"
Api_key = "71af6b0f317cec623a632595d80c6f8e"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Api_key}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('City:', data['name'])
    print('The Weather is', data['weather'][0]['description'])
    print('The Temperature is', data['main']['temp'])
    print('The Pressure is', data['main']['pressure'])
    print('The Humidity is', data['main']['humidity'])
    print('The Visibility is', data['visibility'])
    

