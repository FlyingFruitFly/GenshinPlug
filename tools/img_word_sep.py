import cv2
import numpy as np


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
