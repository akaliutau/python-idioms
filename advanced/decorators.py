from functools import wraps
from time import time, sleep


# Step 1 - define wrapper(s) with function to wrapper as arg
def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()  # code to be executed before wrapped function invoking
        func(*args, **kwargs)  # invoke wrapped function
        print(
            f'measure anno: {func.__name__} finished in {time() - t} sec:')  # code to be executed after wrapped function invoking

    return wrapper


def nullable(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            print('nullable anno: function did not return anything')
        return result

    return wrapper


# decorators factory
def validate(param, threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if kwargs is not None and param in kwargs and kwargs[param] < threshold:
                raise Exception('validate anno: exception: argument must be >= 0')

        return wrapper

    return decorator


# a minimal decorator without @wraps
def minimal(arg):
    print(f'minimal anno: this code has been invoked before {arg}')
    return arg


# Step 2 - annotate wrapping functions with decorator(s)
@measure
@nullable
@validate('sleep_time', 0)
def test(sleep_time=0.1):
    """Delay function - stops current thread for n sec """
    sleep(sleep_time)


@minimal
def test_method(arg1=0):
    print(f'invoking test_method with arg1={arg1}')


def main():
    test(sleep_time=0.3)
    print(f'function\'s name: {test.__name__}, description: {test.__doc__}')

    try:
        test(sleep_time=-10)
    except Exception as e:
        print(e)

    test_method(arg1=2)


if __name__ == '__main__':
    main()
