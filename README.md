# ygo-card-downloader
 Python utility to download all Yu-Gi-Oh! card images from the db.ygoprodeck.com API

To use, either run the main.py script in an IDE of your choice or use a command line tool in the root directory of the application.

```
python main.py
```
Currently this is a very barebones utility that does not utilise any special commands, initially it was for the purpose of a Django project that never worked out. Hopefully this can be of use to someone.

At this time there is a hardcoded 1 second delay between each image download to respect the  recommendations here : https://db.ygoprodeck.com/api-guide/

```
Card images can be pulled from our Google Cloud server but please only pull an image once and then store it locally.
If we find you are pulling a very high volume of images per second then your IP will be blacklisted and blocked.
```