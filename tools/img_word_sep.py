import cv2
import numpy as np
from PIL import Image, ImageOps
import pytesseract


def h_projection(image):
    projection = np.zeros(image.shape, np.uint8)
    # 图像高与宽
    (h, w) = image.shape
    # 长度与图像高度一致的数组
    h_ = [0] * h
    # 循环统计每一行白色像素的个数
    for y in range(h):
        for x in range(w):
            if image[y, x] == 255:
                h_[y] += 1
    # 绘制水平投影图像
    for y in range(h):
        for x in range(h_[y]):
            projection[y, x] = 255

    return h_


def sep(pil_img):
    cv_img = cv2.cvtColor(np.asarray(pil_img), cv2.COLOR_RGB2GRAY)
    temp, img = cv2.threshold(cv_img, 200, 255, cv2.THRESH_BINARY)
    hp = h_projection(img)
    start = 0
    h_start = []
    h_end = []
    # 根据水平投影获取垂直分割位置
    for i in range(len(hp)):
        if hp[i] > 0 and start == 0:
            h_start.append(i)
            start = 1
        if hp[i] <= 0 and start == 1:
            h_end.append(i)
            start = 0
    return h_start, h_end


def get_attr(pil_img):
    h_start, h_end = sep(pil_img)
    (w, h) = pil_img.size
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