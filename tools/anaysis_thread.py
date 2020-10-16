import threading
from PIL import ImageOps
import pytesseract


class ThreadControl(threading.Thread):
    def __init__(self, thread_id, name, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        print("开始线程：" + self.name)
        self.func(*self.args, **self.kwargs)


class AnalysisThread(ThreadControl):
    def __init__(self, work_id, img, save_list, ana_type):
        super().__init__(work_id, 'img_analysis{}'.format(work_id), self.img_dealing, img, save_list, work_id, ana_type)

    @staticmethod
    def img_dealing(img, save_list, work_id,ana_type):
        img = ImageOps.invert(img)
        text_word = pytesseract.image_to_string(img, lang='chi_sim', config='--psm 7')[:-2]\
            .replace(' ', '').replace(',', '')
        print(text_word)
        save_list[work_id][ana_type] = text_word
