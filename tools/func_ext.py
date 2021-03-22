from threading import Thread


def func_ext(func, **kwargs):
    return lambda event: func(event, **kwargs)


def func_thread(func, **kwargs):
    Thread(target=func, kwargs=kwargs).start()



def func_ext_thread(func, **kwargs):
    return lambda: func_thread(func, **kwargs)