import re

PAT1 = r"\w+"
PAT2 = r"\w+\s\w+"
PAT3 = r"\w+\s\w+\s\w+"

MAX_WORDS = 20

def getWords(s, pat):
    PATTERN = pat
    rgx = re.compile(PATTERN)

    freq_dict = dict()

    for it in rgx.finditer(s):
        if *it in freq_dict:
            freq_dict[*it] +=1
        else:
            freq_dict[*it] = 1
    return freq_dict

if __name__ == '__main__':
    fname = input('file name:')
    fname = 'Romans.txt'
    with open(fname, "r", encoding="utf-8") as inp:
        s = inp.read()
        print(s)

        print("words")
        k = 0
        for x, y in getWords(s, PAT1).items():
            print(f"word {x} frequency is {y}", end = "\n")
            break

        for x, y in getWords(s, PAT2|PAT3).items():
            print(f"collocation {x} frequency is {y}", end = "\n")
            if k>MAX_WORDS:
                break
