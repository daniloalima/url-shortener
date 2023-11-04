import requests
import os
import dotenv
from datetime import datetime

def shorten(full_link):
    API_KEY = (os.getenv('API_KEY'))
    base_url = 'https://cutt.ly/api/api.php'

    today = datetime.now()
    date_formated = today.strftime('%d-%M')

    payload = {'key': API_KEY, 'short': full_link, 'name': f'dan-fvtt{date_formated}'}

    req = requests.get(base_url, params=payload)
    data = req.json()

    try:
        short_link = data['url']['shortLink']
        print(short_link)

    except Exception as ex:
        print(f'{data["url"]["status"]} \n {ex}')


if __name__ == "__main__":
    dotenv.load_dotenv()
    shorten('google.com')
