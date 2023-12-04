import random
import time
import requests
from bs4 import BeautifulSoup as bs
from constants import PSN_TROPHIES_URL
from utils import format_hours


game_name = "REMNANT" # TEST
url = f"{PSN_TROPHIES_URL}/search/guides?q={game_name}"
html = requests.get(url)
time.sleep(random.randint(2, 5))

code = bs(html.content, features="html.parser")
guide_cards = code.find_all(class_="guide-page-info")
url = f"{PSN_TROPHIES_URL}{guide_cards[0].contents[1].attrs["href"]}"

html = requests.get(url)
time.sleep(random.randint(2, 5))

code = bs(html.content, features="html.parser")
guide_cards = code.find_all(class_="tag")
hours = format_hours(guide_cards[2].text.replace("\n",""))
