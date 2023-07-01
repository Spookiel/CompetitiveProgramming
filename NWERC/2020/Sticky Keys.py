
from collections import Counter


s = Counter(input())
s2 = Counter(input())


res = ""
for j in s.keys():
    if j in s2.keys():
        if s[j]*2 == s2[j]:
            res += j
print(res)
