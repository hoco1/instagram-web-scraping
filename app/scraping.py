import requests
from datetime import datetime
import json
from decouple import config

url = 'https://www.instagram.com/data/shared_data/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

time = int(datetime.now().timestamp())

session = requests.Session()
response = session.get(url)

csrf = json.loads(response.text)['config']['csrf_token']

username=config("instagramUsername")
password=config("instagramPassword")


payload = {
    'username': username,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
    'queryParams': {},
    'optIntoOneTap': 'false'
}

login_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/accounts/login/",
    "x-csrftoken": csrf
}

# login_response = requests.post(login_url, data=payload, headers=login_header)
# cookies = login_response.cookies.get_dict()