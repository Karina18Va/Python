def tracing(f):
    depth = 0

    def _tracing(*args, **kwargs):
        nonlocal depth
        depth += 1
        print("Входимо у функцію {}".format(f.__name__), end="; ")
        print("глибина: {}".format(depth), end="; ")
        print("позиційні параметри: {}".format(args), end="; ")
        print("ключові параметри: {}".format(kwargs))
        res = f(*args, **kwargs)
        print("Вихід з функції: {}".format(f.__name__), end="; ")
        print("глибина: {}".format(depth), end="; ")
        print("результат: {}".format(res))
        depth -= 1
        return res
    return _tracing


def tracing_class(cls):
    for name, attr in cls.__dict__.items():
        if not name.startswith("__") and callable(attr):
            setattr(cls, name, tracing(attr))
    return cls


@ tracing_class
class SimpleClass:

    def __init__(self):
        pass

    def f(self, *args, **kwargs):
        if kwargs:
            self.f(*args)

    def h(self):
        return 1


if __name__ == '__main__':
    d = SimpleClass()
    d.f(1, 2, y=1)
    d.f(1)
    d.h()