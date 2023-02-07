def print_kwargs(func):
    """ Print Function Key Word Arguments"""
    def wrapper(*args, **kwargs):
        print(f"Function Key Word Arguments : {kwargs}")
        return func(*args, **kwargs)
    return wrapper
