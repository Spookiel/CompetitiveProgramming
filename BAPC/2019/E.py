import sys

sys.setrecursionlimit(10000)
from functools import lru_cache

num = int(input())

@lru_cache(maxsize=None)
def solve(n):
    end = n%10
    if n < 10:
        return min(end, 10-end+1)
    vals = [end + solve(n // 10), 10 - end + solve(n // 10 + 1)]
    return min(vals)


print(solve(num))



