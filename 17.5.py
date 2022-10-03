def decorator(n=float):
    def _decorator(f):
        def __decorator(*args, **kwargs):
            for x in args:
                if type(x) != n:
                    raise TypeError('Задані параметри іншого типу')
            for y in kwargs.values():
                if type(y) != n:
                    raise TypeError('Задані параметри іншого типу')
            res = f(*args, **kwargs)
            return res
        return __decorator
    return _decorator
@decorator(float)
def function(*args, **kwargs):
    n = len(args) + len(kwargs)
    s = 0
    for x in args:
        s += x
    for y in kwargs.values():
        s += y
    return f"Середнє значення: {s/n}"
if __name__ == "__main__":
    print(function(5.0, 8.0, y1=9.0, x1=1.0))