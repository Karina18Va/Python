import os
import sys

def  compareFolders(dir1, dir2):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    dif = files1.difference(files2)
    for item in dif:
        cur_dir = os.getcwd()
        path = os.path.join(cur_dir, item)
        print(path)



if __name__ == "__main":

    res_file = input("File for result:")
    out_res = open(res_file, "w", encoding="utf-8")

    oldout = sys.stdout
    sys.stdout = out_res
    dir1 = input("Folder1:")
    dir2 = input("Folder2:")




    compareFolders(dir1, dir2)
    out_res.close()
    
    sys.stdout = oldout
