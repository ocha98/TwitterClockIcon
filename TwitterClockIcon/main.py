import datetime
import os
from dotenv import load_dotenv
from .twitter_api import UpdateProfileIcon
from .util import time_rotate_image

load_dotenv()

API_KEY = os.environ['API_KEY']
API_KEY_SECRET = os.environ['API_KEY_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

def main():
    api = UpdateProfileIcon(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    timezone = datetime.timezone(datetime.timedelta(hours = 9))
    date = datetime.datetime.now(tz = timezone)

    # 夜は眠っているアイコン
    fillcolor = (115, 174, 232)
    if 21 <= date.hour < 24 or 0 <= date.hour < 7:
        time_rotate_image("img/night.png", timezone, fillcolor = fillcolor)
    else:
        time_rotate_image("img/normal.png", timezone, fillcolor = fillcolor)

    api.update_profile_icon("img/rotated.png")
