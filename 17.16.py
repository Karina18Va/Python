def decorator_line(func):
    def _decorator_line(*args, **kwargs):
        _decorator_line.count += 1
        print(_decorator_line.count)
        res = func(*args, **kwargs)
        return res
    _decorator_line.count = 0
    return _decorator_line

@decorator_line
def wrt(line):
    print(lines)

if __name__ == "__main__":
    d = 1
    f = open("file.txt", "r")
    for lines in f.readlines():
        wrt(lines)
