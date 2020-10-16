import threading


class ThreadControl(threading.Thread):
    def __init__(self, thread_id, name, counter, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        print("开始线程：" + self.name)
        self.func(*self.args, **self.kwargs)


class AnalysisThread(ThreadControl):
    def __init__(self, img):
        super().__init__()
