combs = []
def place(lastpos, left, msize,acc=[]):
    if left == 0:
        combs.append(acc)
    for i in range(lastpos+2, msize-1):
        place(i, left-1, msize, acc+[i])


n,m = list(map(int, input().split()))
grid = [input() for i in range(n)][::-1]

tot = 0
for can in range(1, m//2 + 1):
    place(-2,can,m)
    tot += len(combs)

INF = 9999999
dp = [[INF for _ in range(len(combs))] for i in range(n+1)]
dp[0] = [0 for j in range(len(combs))]

for row in range(2, n+1, 2):
    for lconfig in range(len(combs)):
        low_covered = [0]*m
        for j in combs[lconfig]:
            low_covered[j] = 1
            low_covered[j+1] = 1
        for new_config in range(len(combs)):
            cans = combs[new_config]
            valid_row = True
            high_covered = [0]*m
            for can in cans:
                if not low_covered[can] and not low_covered[can+1]:
                    valid_row = False
                    break
                high_covered[can] = 1
                high_covered[can+1] = 1
            if not valid_row:
                # Missing a support so can't use this new_config on this row
                continue

            # Now need to check the actual cangaroo is covered
            covered = True
            for hcol in range(m):
                if grid[row-1][hcol]=="#" and not high_covered[hcol]:
                    covered = False
                    break
                if grid[row-2][hcol]=="#" and not high_covered[hcol]:
                    covered = False
                    break
            if not covered:
                # Cangaroo wasn't covered by this config
                continue
            dp[row][new_config] = min(dp[row][new_config], dp[row-2][lconfig]+len(cans))

tallest_point = -1
# Set to -1 to deal with empty grid case
for row in range(0, n, 2):
    for col in range(m):
        if grid[row][col] == "#":
            tallest_point = max(tallest_point, row)
        if grid[row+1][col] == "#":
            tallest_point=max(tallest_point, row+1)

if tallest_point%2 == 0:
    ### Lower row so add one
    tallest_point += 1

print(min(dp[tallest_point+1]))


