# !/usr/bin/python3
# -*- coding: utf-8 -*-

from Paimon.Paimon import Paimon
import tkinter


if __name__ == '__main__':
    root = tkinter.Tk()
    root.withdraw()
    paimon = Paimon()
    paimon.start()
    root.mainloop()
