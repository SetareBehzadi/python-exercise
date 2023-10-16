from datetime import datetime


def log_time(func):
    def wrapped_func(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        duration = end - start
        hour = duration.seconds // 3600
        minute = duration.seconds // 60
        second = duration.seconds % 60
        print(
            f"Elapsed time: {hour}: {minute}: {second}"
        )
        return result
    return wrapped_func
