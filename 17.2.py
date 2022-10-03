def ininterval(a, b):
    def _mydecorator(function):
        def __mydecorator(*args, **kw):
            # виконати дії перед викликом реальної ункції
            res = function(*args, **kw)
            # виконати дії після виклику функції
            if res < a or res > b:
                res = (a + b) / 2

            return res

        # повренути підфункцію
        return __mydecorator

    return _mydecorator



@ininterval(0, 1)
def f3(x):
    return 2 * x - 1

@ininterval(0, 2)
def f4(x, y):
    return -1



if __name__ == '__main__':
    print("{}".format(f3(1)))
    print("{}".format(f3(-3)))
    print("{}".format(f4(1, 4)))

