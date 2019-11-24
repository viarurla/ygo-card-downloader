import requests
from os import path
import time
import json
import settings


class CardManager:

    def get_json_file(self):
        time.sleep(1)
        url = settings.api_url
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open('./cards.json', 'wb') as f:
                f.write(r.content)
        else:
            print(r.status_code)
            print('Request failed')

    def download_card_image(self, card_id):
        if not path.exists(f'./cards/{card_id}.jpg'):
            time.sleep(1)
            url = settings.api_images_url + f'{card_id}.jpg'
            r = requests.get(url, stream=True)
            if r.status_code == 200:
                with open(f'./cards/{card_id}.jpg', 'wb') as image:
                    for chunk in r.iter_content(1024):
                        image.write(chunk)
            else:
                print(url)
                print(r.status_code)
        else:
            print('Already Exists')

    def process_json(self):
        with open('./cards.json', 'rb') as f:
            cards = json.load(f)
            for card in cards:
                self.download_card_image(card['id'])

                print(f"Downloaded {card['name']}: {card['id']} primary art")

                if len(card['card_images']) > 1:
                    # We should already have the first card
                    for card_image in card['card_images'][1:]:
                        self.download_card_image(card_image['id'])
                        print(f"Downloaded {card['name']}: {card['id']} alternate art")
