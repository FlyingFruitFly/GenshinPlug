from mss import mss
from PIL import Image

import tools.get_attributes
from tools.window_locate import get_genshin_window
# from exceptions import ToolsNotFound


def screenshot(mon):
    with mss() as sct:
        sct_img = sct.grab(mon)
        screen_shot = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
    return screen_shot


def get_attributes_img(cut_percent):
    if tools.get_attributes.flag:
        mss()
        tools.get_attributes.flag = False
    shape = get_genshin_window()
    mon = {"left": shape[0], "top": shape[1], "width": shape[2] - shape[0], "height": shape[3] - shape[1]}
    mon["left"] = mon["left"] + int(mon["width"] * cut_percent[0])
    mon["top"] = mon["top"] + int(mon["height"] * cut_percent[1])
    mon["width"] = int(mon["width"] * (cut_percent[2] - cut_percent[0]))
    mon["height"] = int(mon["height"] * (cut_percent[3] - cut_percent[1]))
    return screenshot(mon)


