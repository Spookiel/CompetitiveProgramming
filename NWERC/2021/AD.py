

def read_reply():
    a = input().split()
    if "GRANTED" in a:
        return -1
    return int(a[2][1:])

ans = "a"

### First thing is to guess the length
size = 1
while True:
    print(ans, flush=True)
    got = read_reply()
    if got == 5:
        ans += "a"
        size += 1
    else:
        break


def calc_correct(rep):
    assert (rep-14)%9 == 0
    return (rep-14)//9

### So now we have the length
### Just going to guess each character at a time

from string import ascii_letters

ans = ["a"]*size
pos = 0
lastcorrect = 0
while True:
    print("".join(ans), flush=True)
    rep = read_reply()
    if rep == -1:
        break
    correct = calc_correct(rep)
    if correct > lastcorrect:
        pos = 0
        lastcorrect = correct
    else:
        pos += 1
        ans[correct] = ascii_letters[pos]



