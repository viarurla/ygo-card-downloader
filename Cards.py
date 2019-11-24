import requests
from os import path
import time
import json


class CardManager:

    def get_json_file(self):
        time.sleep(1)
        url = 'https://db.ygoprodeck.com/api/v5/cardinfo.php'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open('./cards.json', 'wb') as f:
                f.write(r.content)
        else:
            print(r.status_code)
            print('Request failed')

    def download_card_image(self, card_id):
        if not path.exists(f'cards/{card_id["id"]}.jpg'):
            time.sleep(1)
            url = f'https://storage.googleapis.com/ygoprodeck.com/pics/{card_id["id"]}.jpg'
            r = requests.get(url, stream=True)
            if r.status_code == 200:
                with open(f'cards/{card_id["id"]}.jpg', 'wb') as image:
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
                self.download_card_image(card)

                print(f"Downloaded {card['name']} primary art")

                if len(card['card_images']) > 1:
                    # We should already have the first card
                    for card_image in card['card_images'][1:]:
                        self.download_card_image(card_image['id'])

                        print(f"Downloaded {card['name']} alternate art")