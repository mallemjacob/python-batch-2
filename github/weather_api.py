import requests, pprint

weather_api = 'https://api.weatherstack.com/current?access_key=key&query=Guntur,%20India'

response = requests.get(weather_api)


pprint.pprint(output['location']['region'])