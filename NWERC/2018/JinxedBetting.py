input()
p = list(map(int, input().split()))

lead = p[0]
p[0] = -1<<60
p.sort()
gap = lead - p[-1] + 1
f = 1

print(p)
print(gap) ### Gap between Julie and closest better
steps = 0
while gap:
    inc = f.bit_length() - 1
    big = p[-1] - p[-2]
    print(big, "BIG", inc, steps, "HERE", gap, "GAP")
    if big*inc >= gap:
        print("ADDING", gap + (gap-1)//inc)
        steps += gap + (gap-1)//inc
        break
    gap -= inc*big
    steps += (inc+1)*big
    f += 1
    p.pop()
    print(p, steps)

print(steps -1)
