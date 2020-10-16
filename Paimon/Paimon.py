import tkinter
from PIL import Image, ImageTk
from Paimon.method import section
from Paimon.method.mouse_event import move, right_click
from Paimon.settings import height, width
from tools.func_ext import func_ext
from mss import mss

button_bind = [
    {"sequence": "<B1-Motion>", "func": move},
    # ["<Button-1>", left_click],
    {"sequence": "<Button-3>", "func": right_click}
]

menu_settings = [
    {"label": "伤害分析", "command": section.screenshot},
    # {"label": "属性获取", "command": section.onCopy},
    # {"label": "圣遗物录入", "command": section.onCut},
]


class Paimon:

    def set_window(self):
        self.root.overrideredirect(True)
        self.root.wm_attributes('-topmost', 1)
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        root_x = sw - width
        root_y = sh - height - 50
        self.root.geometry(str(width) + "x" + str(height) + "+%d+%d" % (root_x, root_y))

    def set_canvas(self):
        self.canvas.configure(width=width, height=height, highlightthickness=0)
        self.img.thumbnail((width, height))
        self.im = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(width / 2, height / 2, image=self.im)
        for bind_config in button_bind:
            self.canvas.bind(sequence=bind_config["sequence"], func=func_ext(bind_config["func"], window=self))
        self.canvas.pack()

    def set_menu(self):
        for setting in menu_settings:
            self.menu.add_command(**setting)
            self.menu.add_separator()
        self.menu.add_command(label="退出", command=self.root.quit)

    def __init__(self):
        self.im = None
        self.img = Image.open("paimon.jpg")
        self.y = 0
        self.x = 0
        self.root = tkinter.Tk()
        self.set_window()
        self.canvas = tkinter.Canvas(self.root)
        self.set_canvas()
        self.menu = tkinter.Menu(self.canvas, tearoff=0)
        self.set_menu()

    def start(self):
        mss()
        self.ensure_top()
        self.root.mainloop()

    def ensure_top(self):
        self.root.lift()
        # self.root.after(5000, self.ensure_top)
