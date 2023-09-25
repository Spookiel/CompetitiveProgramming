import math
from functools import lru_cache


def bin_dist(n, k, p):
    return getp(k, p, n)

def getp(x, p, N):
    """Returns P(x = X) for a binomial distribution X ~ B(N, p)"""
    return math.comb(N, x) * (p**x) * ((1-p)**(N - x))

def solve_round(rnum, players_left, prob_losing, k, n):
    # players left must have lost exactly k-1 in rnum-1 rounds and then lost in this round
    # and n - players_left must have lost k or more lives in rnum-1 rounds

    prob_one_loses_k = bin_dist(rnum-1, k-1, prob_losing)*prob_losing
    prob_pleft_loses_k = pow(prob_one_loses_k,players_left) * math.comb(n, players_left)
    # prob_one_lose_more = 0
    # for lost_more in range(k, rnum+1):
    #     prob_one_lose_more += bin_dist(rnum-1,lost_more, prob_losing)
    prob_one_lose_more = 0
    for lost_more in range(k):
        prob_one_lose_more += bin_dist(rnum-1,lost_more, prob_losing)
    prob_one_lose_more = 1-prob_one_lose_more
    prob_rest_lose_more = pow(prob_one_lose_more,(n-players_left))
    return prob_rest_lose_more*prob_pleft_loses_k

line = input().split()
people = int(line[0])
lives = int(line[1])
q = float(line[2])
p = 1 - q


ans = 0
last = 0
for round in range(lives, 1200):
    #print(ans)
    ans += solve_round(round, 1, p, lives, people)
print(f"{1 - ans:.9f}")