import time


def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls

    return decorate


def benchmark(f):
    def _benchmark(*args, **kwargs):
        t = time.perf_counter()
        res = f(*args, **kwargs)
        t = time.perf_counter() - t

        print("Benchmark is", t)
        print(f.__name__)
        return res

    return _benchmark


@for_all_methods(benchmark)
class Btree:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self):
        return self.y + self.x


if __name__ == '__main__':
    obj1 = Btree(10, 5)
    print(obj1.calculate())