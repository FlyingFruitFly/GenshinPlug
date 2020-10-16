import pytesseract
from PIL import ImageOps

from tools.img_word_sep import sep
from tools.screenshot import get_attributes_img
from tools.anaysis_thread import AnalysisThread
from Paimon.settings import attribute_words, sep_attribute

character = (0.135, 0.05, 0.865, 1)


def get_character_attributes():
    img = get_attributes_img(character)
    return get_attr(img)


def get_attr(pil_img):
    h_start, h_end = sep(pil_img)
    (w, h) = pil_img.size
    h_len = len(h_end)
    thread_pool = []
    result_text = [['', '']for i in range(h_len)]
    for i in range(h_len):
        # 获取行图像
        box = (0, max(h_start[i]-5, 0), int(w/2), min(h_end[i]+5, h))
        sep_word = pil_img.crop(box)
        ana = AnalysisThread(i, sep_word, result_text, 0)
        thread_pool.append(ana)
        ana.start()

        box = (int(w/2), max(h_start[i]-5, 0), w, min(h_end[i]+5, h))
        sep_num = pil_img.crop(box)
        ana = AnalysisThread(i, sep_num, result_text, 1)
        thread_pool.append(ana)
        ana.start()
    for thread in thread_pool:
        thread.join()
    result = {}
    for attr in result_text:
        if attr[0] in attribute_words.keys():
            attr_name = attribute_words[attr[0]]
            if attr_name in sep_attribute:
                attr_value = attr[1].split('+')
                result['Base' + attr_name] = attr_value[0]
                result['Addi' + attr_name] = attr_value[1]
            else:
                result[attr_name] = attr[1]
    return result
