import pytesseract
from PIL import ImageOps

from tools.img_word_sep import sep
from tools.screenshot import get_attributes_img

character = (0.135, 0.05, 0.865, 1)


def get_character_attributes():
    img = get_attributes_img(character)
    get_attr(img)


def get_attr(pil_img):
    h_start, h_end = sep(pil_img)
    (w, h) = pil_img.size
    thread_pool = []
    for i in range(len(h_start)):
        # 获取行图像
        box = (0, max(h_start[i]-5, 0), int(w/2), min(h_end[i]+5, h))
        sep_word = pil_img.crop(box)
        sep_word = ImageOps.invert(sep_word)
        text_word = pytesseract.image_to_string(sep_word, lang='chi_sim', config='--psm 7')[:-2].replace(' ', '')
        print(text_word)

        box = (int(w/2), max(h_start[i]-5, 0), w, min(h_end[i]+5, h))
        sep_num = pil_img.crop(box)
        sep_num = ImageOps.invert(sep_num)
        text_num = pytesseract.image_to_string(sep_num, lang='chi_sim', config='--psm 7')[:-2].replace(',', '').replace(' ', '')
        print(text_num)