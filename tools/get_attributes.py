import pytesseract

from tools.screenshot import get_attributes_img
from tools.img_word_sep import get_attr

character = (0.135, 0.05, 0.865, 1)


def get_character_attributes():
    img = get_attributes_img(character)
    get_attr(img)
