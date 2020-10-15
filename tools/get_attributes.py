import pytesseract

from tools.screenshot import get_attributes_img

character_word = (0.14, 0.05, 0.86, 1)
sep = 40


def get_character_attributes():
    img = get_attributes_img(character_word)
    height = int(img.height * 2 / sep)
    width = img.width
    for i in range(sep-1):
        box = (0, height * i, width, int(height * (i + 1.5)))
        sep_word = img.crop(box)
        if i < 10:
            sep_word.save(r'C:\Users\49165\Desktop\GenshinPlug\word{}.png'.format(i))
            print(pytesseract.image_to_string(sep_word, lang='chi_sim'), '\n')

