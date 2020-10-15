def func_ext(func, **kwargs):
    return lambda event: func(event, **kwargs)
