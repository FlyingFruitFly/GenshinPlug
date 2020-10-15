import win32gui


def get_genshin_window(window_name='原神'):
    hwnd = win32gui.FindWindow(0, window_name)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    return left, top, right, bottom
