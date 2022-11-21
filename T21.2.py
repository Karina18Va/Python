import re

s = input("Input text")

# find all words

PATTERN = "[a-z, A-Z]+"
rr = re.compile(PATTERN)

res = rr.findall(s)
print(res)

def printWords(fname, pattern):
    rgx = re.compile(pattern)

    with open(fname, 'r') as f:
        rows = f.readline()
        for row in rows:
            for word in rgx.finditer(rows):
                print(word, end = '\n')

SENTENCE = r"\b[A-ZА-ЯІЇЄ].*?[\.\!\?](?<![A-ZА-ЯІЇЄ\.][a-zа-яіїє]\.)(?=\s|$)"

if __name__ == "__main__":
    fn = "3.txt"
    rexp = SENTENCE
    printWords(fn, rexp)