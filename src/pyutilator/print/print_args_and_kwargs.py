def print_args_and_kwargs(func):
    def inner(*args, **kwargs):
        for arg in args:
            print("%s" % arg)
        for key, value in kwargs.items():
            print("%s : %s" % (key, value))
    return inner
