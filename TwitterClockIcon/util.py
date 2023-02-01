from PIL import Image
import datetime

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