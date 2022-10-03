def makegreaterzero(function):
    def _mydecorator(*args, **kw):
        # виконати дії перед викликом реальної ункції
        res = function(*args, **kw)
        # виконати дії після виклику функції
        if res < 0:
            res = -res
        elif res == 0:
            res = 1

        return res

    # повренути підфункцію
    return _mydecorator


@makegreaterzero
def f(x):
    return 2 * x - 1


if __name__ == '__main__':
    print("{}".format(f(2)))
    print("{}".format(f(-3)))



