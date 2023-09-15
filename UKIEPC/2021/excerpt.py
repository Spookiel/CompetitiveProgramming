

import random
from collections import deque


def check_sub(smaller, big):
    i = 0
    for j in range(len(big)):
        if smaller[i] == big[j]:
            i += 1
        if i == len(smaller):
            return True

    return False



def attempt(s1,s2):
    n = len(s1)

    chosen = []

    s1 = deque(s1)
    s2 = deque(s2)

    while len(chosen) < (n+1)//2:

        if len(s1) >= len(s2):
            c = s1.popleft()
            r = []
            for k in range(3):
                a = s2.popleft()
                if c == a:
                    chosen.append(c)
                    break
                r.append(a)
            for j in reversed(r):
                s2.appendleft(j)
        else:
            r = []
            c = s2.popleft()
            for k in range(3):
                a = s1.popleft()
                if c == a:
                    chosen.append(c)
                    break
                r.append(a)
            for j in reversed(r):
                s1.appendleft(j)
    print(len(chosen))


    res = check_sub(chosen, s2)
    res1 = check_sub(chosen, s1)
    if res and res1:
        return "".join(chosen)
    return False



n = int(input())
s1 = input()
s2 = input()

tries = 0
while True:
    got = attempt(s1, s2)
    if got:
        print(got)
        break
    tries += 1
    if tries%100 == 0:
        print(tries)



"""
20
GACTAGCGATTGACAGAGTC
ACCCAGGAAAGAACATTCGC
"""