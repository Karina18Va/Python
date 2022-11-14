import os
import sys
from datetime import datetime, timedelta


def compareFolders3(dir1, dir2):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    dif = files1.intersection(files2)
    res = ()
    for item in dif:
        cur_dir = os.getcwd()
        path1 = os.path.join(cur_dir, dir1, item)
        path2 = os.path.join(cur_dir, dir2, item)
        t1 = os.path.getctime(path1)
        t2 = os.path.getctime(path2)
        time_diff = timedelta(t1 - t2)
        if t1 == t2:
            continue
        else t1>t2:
            size_diff = os.path.getsize(path1) - os.path.getsize(path1)
            res[path1] = "diff time is {} hr, size diff {} b".format(time_diff.hours, size_diff)
    print(res)




if __name__ == "__main":
    res_file = input("File for result:")
    out_res = open(res_file, "w", encoding="utf-8")

    oldout = sys.stdout
    sys.stdout = out_res

    if len(sys.argv) < 3:
        print("Not enough input arguments, format is:")
        print("/script dir1 dir2")
        return

    dir1 = sys.argv[1]
    dir2 = sys.argv[2]

    compareFolders3(dir1, dir2)
    out_res.close()

    sys.stdout = oldout
