from Paimon.settings import height, width


def move(event, window):
    new_x = (event.x - window.x) + window.root.winfo_x() - int(width/2)
    new_y = (event.y - window.y) + window.root.winfo_y() - int(height/2)
    s = str(width) + "x" + str(height) + "+" + str(new_x) + "+" + str(new_y)
    window.root.geometry(s)


def right_click(event, window):
    menu = window.menu
    menu.post(event.x_root, event.y_root)