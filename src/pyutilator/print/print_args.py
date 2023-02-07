def print_args(func):
    """ Print function Arguments"""
    def wrapper(*args, **kwargs):
        print(f"Function Arguments : {args} ")
        return func(*args, **kwargs)
    return wrapper
