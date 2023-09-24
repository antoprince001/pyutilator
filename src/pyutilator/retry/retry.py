import functools


class MaxRetriesExceededException(Exception):
    """Custom exception class for maximum retries reached."""
    def __init__(self, message="Max retries reached."):
        super().__init__(message)


def retry(max_retries=3):
    """ Retry Function execution until maximum retries
    Parameters:
    - max_retries (int, optional): The maximum number of times to retry the function call.
      Default is 3.
    """
    if not isinstance(max_retries, int):
        raise TypeError("max_retries must be an integer")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Execution caught: {e}. Retrying ...")
            raise MaxRetriesExceededException()
        return wrapper
    return decorator
