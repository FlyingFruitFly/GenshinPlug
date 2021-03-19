import tkinter
from PIL import Image, ImageTk
from Paimon.method import section
from Paimon.method.section import character_attributes
from Paimon.method.mouse_event import move, right_click
from Paimon.settings import height, width, img_height, attribute_height, attribute_apparent
from tools.func_ext import *
from mss import mss

button_bind = [
    {"sequence": "<B1-Motion>", "func": move},
    # ["<Button-1>", left_click],
    {"sequence": "<Button-3>", "func": right_click}
]

menu_settings = [
    {"label": "获取人物属性", "command": section.add_attributes},
    {"label": "获取人物元素", "command": section.get_element},
    {"label": "清空全部属性", "command": section.del_attributes},
    # {"label": "生成分析报告", "command": section.onCopy},
]


def generate_attribute_text():
    text = ''
    for attr, attr_name in attribute_apparent.items():
        if attr in character_attributes.keys():
            attr_value = character_attributes[attr]
        else:
            attr_value = '无'
        text += attr_name + ': ' + attr_value + '\n'
    return text


class Paimon:

    def set_window(self):
        self.root.overrideredirect(True)
        self.root.wm_attributes('-topmost', 1)
        self.root.attributes("-alpha", 0.7)
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        root_x = sw - width
        root_y = sh - height - 50
        self.root.geometry(str(width) + "x" + str(height) + "+%d+%d" % (root_x, root_y))

    def set_canvas(self):
        self.canvas.configure(width=width, height=height, highlightthickness=0)
        self.img.thumbnail((width, img_height))
        self.im = ImageTk.PhotoImage(self.img)
        for bind_config in button_bind:
            self.canvas.bind(sequence=bind_config["sequence"], func=func_ext(bind_config["func"], window=self))
        self.canvas.pack()
        self.canvas.create_image(width / 2, img_height / 2, image=self.im)
        self.attribute_box = self.canvas.create_text(width/2, img_height+int(attribute_height/2),
                                                     text=generate_attribute_text(), font="time 12 bold")

    def set_menu(self):
        for setting in menu_settings:
            self.menu.add_command(label=setting['label'], command=func_ext_thread(setting['command'], paimon=self))
            self.menu.add_separator()
        self.menu.add_command(label="退出", command=self.root.quit)

    def __init__(self):
        self.im = None
        self.img = Image.open("paimon.jpg")
        self.y = 0
        self.x = 0
        self.attribute_box = None
        self.root = tkinter.Toplevel()
        self.set_window()
        self.canvas = tkinter.Canvas(self.root)
        self.set_canvas()
        self.menu = tkinter.Menu(self.canvas, tearoff=0)
        self.set_menu()
        paimon = self

    def start(self):
        mss()
        self.ensure_top()
        self.root.mainloop()

    def ensure_top(self):
        self.root.lift()
        self.root.after(5000, self.ensure_top)

    def update_attribute(self):
        self.canvas.delete(self.attribute_box)
        self.attribute_box = self.canvas.create_text(width/2, img_height+int(attribute_height/2),
                                                     text=generate_attribute_text(), font="time 12 bold")
