# !/usr/bin/python3
# -*- coding: utf-8 -*-

from Paimon.Paimon import Paimon


if __name__ == '__main__':
    paimon = Paimon()
    paimon.start()
    print("退出主线程")
