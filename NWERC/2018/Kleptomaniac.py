n,m = list(map(int, input().split()))

s = list(map(ord, input()))
t = list(map(ord, input()))

for i in range(len(t)):
    t[i] -= 97
for j in range(len(s)):
    s[j] -= 97


plain = [0]*(m-n) + s
#print(plain)
for j in range(m-n-1, -1,-1):
    plain[j] = (t[j+n]-plain[j+n]) % 26

for i in plain:
    print(chr(i+97), end="")

