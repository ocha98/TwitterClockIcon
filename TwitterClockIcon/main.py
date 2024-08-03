import datetime
import os
from dotenv import load_dotenv
import tweepy
from PIL import Image
import datetime

load_dotenv()

API_KEY = os.environ['API_KEY']
API_KEY_SECRET = os.environ['API_KEY_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

def time_rotate_image(img_path,
                      save_path,
                      timezone,
                      fillcolor = (0, 0, 0),
                      ):
    """
    アイコンの頭部を時計の短針の位置へ回転した画像を生成する
    画像はsave_pathの場所に保存される
    回転角は1時間刻み
    """
    img = Image.open(img_path)
    date = datetime.datetime.now(tz=timezone)
    arg = date.hour%12 * 360//12
    rotated_img = img.rotate(360 - arg, fillcolor=fillcolor)
    rotated_img.save(save_path)

def main():
    timezone = datetime.timezone(datetime.timedelta(hours = 9))
    date = datetime.datetime.now(tz = timezone)

    # 夜は眠っているアイコン
    save_path = "/tmp/rotated.png"
    fillcolor = (115, 174, 232)
    if 21 <= date.hour < 24 or 0 <= date.hour < 7:
        time_rotate_image("img/night.png", save_path, timezone, fillcolor = fillcolor)
    else:
        time_rotate_image("img/normal.png", save_path, timezone, fillcolor = fillcolor)

    auth = tweepy.OAuth1UserHandler(
        API_KEY,
        API_KEY_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET,
        )
    api = tweepy.API(auth)
    api.update_profile_image(save_path)

    os.remove(save_path)
