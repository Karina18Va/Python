
class ExceptNonEqual(Exception):

    def __init__(self):
        super()

    def __str__(self):
        return "Non Equal sizes!!!"


def key_value_equal_sizes(fun):
    def _key_value_equal_sizes(*args, **kwargs):
        if len(args) != len(kwargs):
            raise ExceptNonEqual
        res = fun(*args, **kwargs)
        return res

    return _key_value_equal_sizes


@key_value_equal_sizes
def func1(*args, **kwargs):
    p = 1
    for x, y in zip(args, kwargs.values()):
        if y == 0:
            continue
        p *= (x + 1 / y)

    return p


if __name__ == '__main__':

    a1 = func1(1, 2, 3, y1=1, y2=2, y3=3)
    print("a=", a1)

    try:
        a1 = func1(1, 2, 3, y1=1, y2=2)
        print("a=", a1)
    except ExceptNonEqual as e:
        print("Caught exception: ", e)