import re


DATE1 = r"\b(?P<y1>\d{1,4})/(?P<m1>\d{1,2})/(?P<d1>\d{1,2})"
DATE2 = r"\b(?P<d2>\d{1,2})\.(?P<m2>\d{1,2})\.(?P<y2>\d{1,4})"
DATE3 = r"\b(?P<y3>\d{1,4})\-(?P<m3>\d{1,2})\-(?P<d3>\d{1,2})"
DATE = DATE1 + "|" + DATE2 + "|" + DATE3


def change(string, n):

    def _change(match):
        date = match.group()
        if "/" in date:
            l = "1"
        elif "." in date:
            l = "2"
        else:
            l = "3"

        u = match.group("u" + l)
        e = match.group("e" + l)
        f = match.group("f" + l)

        while len(u) != 4:
            u = "0" + u
        if len(e) != 2:
            e = "0" + e
        if len(f) != 2:
            f = "0" + f

        if n == 1:
            date = "/".join((u, e, f))
        elif n == 2:
            date = ".".join((f, e, u))
        else:
            date = "-".join((u, e, f))
        return date

    return re.sub(DATE, _change, string)


if __name__ == "__main__":
    n = int(input())

    with open("input.txt", "r", encoding="utf-8") as inp:
        d = inp.read()
        d = change(d, n)
    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(d)