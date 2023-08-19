import sys
sys.setrecursionlimit(100000)
s = input()

from collections import defaultdict
d = defaultdict(int)
translate = dict()
n = int(input())

def weird_sort(word):
    if len(word) <= 2:
        return word
    return word[0]+"".join(sorted(word[1:-1]))+word[-1]

for i in range(n):
    word = input()
    sword = weird_sort(word)
    d[sword] += 1
    translate[sword] = word

#### DP[i] is number of valid sentences ending at character i
MAXWORDLEN = 100
from functools import lru_cache
@lru_cache(maxsize=None)
def count_valid(end):
    global log
    if end == 0:
        return 1

    tot = 0
    for start in range(end-1, max(end-MAXWORDLEN-1, -1), -1):
        word = weird_sort(s[start:end])
        diff = count_valid(start)*d[word]
        tot += diff
    return tot
res = count_valid(len(s))
if res == 0:
    print("impossible")
elif res >= 2:
    print("ambiguous")
else:
    ### Need to extract the words here
    ans = []
    last = len(s)
    for i in range(len(s)-1,-1,-1):
        word = weird_sort(s[i:last])
        if count_valid(i) and word in translate:
            ans.append(translate[word])
            last = i
    ans = reversed(ans)
    for i in ans:
        print(i, end=" ")