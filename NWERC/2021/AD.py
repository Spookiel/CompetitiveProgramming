

def read(x):
    print(x, flush=True)
    reply = input()
    if "GRANTED" in reply:
        return 0
    return int(reply.split()[2][1:])

l = 1
while True:
    reply = read("a"*l)
    if reply != 5:
        break
    l += 1
ans = ["a"]*l


lrep = 0
pos = 0
from string import ascii_letters, digits
s = ascii_letters+digits
while True:
    reply = read("".join(ans))
    if not reply:
        break
    ans[(reply-14)//9] = s[pos]
    if lrep != reply:
        pos = 0
    else:
        pos += 1
    lrep = reply

print("".join(ans), flush=True)
#print("Hunter2", flush=True)