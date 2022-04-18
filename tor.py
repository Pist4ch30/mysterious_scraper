from stem import Signal
from stem.control import Controller
import requests, json


def renew_connection():

    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='jesuisla95')
        controller.signal(Signal.NEWNYM)
        proxies = {
            'http' : 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }
        ip = s.get('https://httpbin.org/ip', proxies=proxies).json()

        print(s.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip["origin"]}', proxies=proxies).text)

s = requests.session()
print(s.get('https://httpbin.org/ip',).text)
a = renew_connection()
