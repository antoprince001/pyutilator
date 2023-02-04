def print_kwargs(func):
    def inner(*args, **kwargs):
        for key, value in kwargs.items():
            print("%s : %s" % (key, value))
    return inner
