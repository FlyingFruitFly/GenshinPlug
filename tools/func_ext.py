def func_ext(func, **kwargs):
    return lambda event: func(event, **kwargs)


def func_ext_no_attr(func, **kwargs):
    return lambda: func(**kwargs)