import random
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from constants import PSN_TROPHIES_URL
from utils import format_hours
from urllib.parse import quote
from datetime import datetime

games_df = pd.read_csv("games.csv")


for game in games_df["GAME"]:
        try:
            print(f"Getting data for: {game}")
            url = f"{PSN_TROPHIES_URL}/search/guides?q={quote(game +' -')}"
            html = requests.get(url)
            # time.sleep(random.randint(1, 3))

            code = bs(html.content, features="html.parser")
            guide_cards = code.find_all(class_="guide-page-info")
            url = f"{PSN_TROPHIES_URL}{guide_cards[0].contents[1].attrs["href"]}"

            html = requests.get(url)
            # time.sleep(random.randint(1, 3))

            code = bs(html.content, features="html.parser")
            guide_cards = code.find_all(class_="tag")
            hours = format_hours(guide_cards[2].text.replace("\n",""))
            games_df.loc[games_df["GAME"] == game, "HOURS"] = hours
        except:
            games_df.loc[games_df["GAME"] == game, "HOURS"] = None
    
print("Creating excel file...")
now = datetime.now()
games_df.to_excel(f"GameList_{now.month}-{now.day}.xlsx", index=False)
