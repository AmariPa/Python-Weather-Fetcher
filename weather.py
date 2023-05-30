import math
import requests

#API Key
KEY = 'ENTER KEY HERE'

URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city name: ')
request_url = f'{URL}?appid={KEY}&q={city}&units=imperial'
response  = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    tempurature = math.ceil(data['main']['temp'])
    print('Weather:', weather)
    print('Tempurature:', tempurature, 'F°')
else:
        print('ERROR')