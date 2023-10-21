import requests
from bs4 import BeautifulSoup
from cachetools import cached, TTLCache
import re


@cached(cache=TTLCache(maxsize=1024, ttl=10800))
def get_imgs(usename):
    # URL of the Telegram webpage
    url = f"https://t.me/s/{usename}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all elements with class 'tgme_widget_message_photo_wrap'
    photo_wraps = soup.find_all(class_="tgme_widget_message_photo_wrap")

    # Extract background images from the style attribute of the elements
    background_images = []
    for photo_wrap in photo_wraps:
        # Extract the URL of the background image using regular expression
        style = photo_wrap.get("style")
        image_url = re.search(r'url\((.*?)\)', style).group(1)
        background_images.append(image_url[1:-1])

    return list(reversed(background_images[-6:]))
