def print_args(func):
    def inner(*args, **kwargs):
        for arg in args:
            print("%s" % arg)
    return inner
